import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import defaultdict, deque
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细


# 案例数据：3个工件，每个工件有4道工序（机器编号，处理时间）
jobs = [
    [(0, 3), (1, 2), (2, 2), (3, 5)],  # 工件0
    [(0, 2), (2, 1), (1, 4), (0, 5)],  # 工件1
    [(3, 4), (0, 3), (2, 1), (1, 6)],  # 工件2
]

# 遗传算法参数
POP_SIZE = 50  # 种群大小
NUM_GENERATIONS = 30  # 迭代次数
CX_PROB = 0.8  # 交叉概率
MUT_PROB = 0.2  # 变异概率


def create_individual(jobs):
    """生成初始个体（随机合法调度序列）"""
    queues = {j: deque(range(len(jobs[j]))) for j in range(len(jobs))}
    # print("queues=", queues)
    individual = []
    while any(queues.values()):
        valid_jobs = [j for j in queues if queues[j]]
        j = random.choice(valid_jobs)
        individual.append((j, queues[j].popleft()))
    return individual


def calculate_makespan(individual, jobs):
    """计算调度序列的makespan"""
    machine_times = defaultdict(int)
    job_times = defaultdict(int)
    job_step = defaultdict(int)
    schedule = []
    makespan = 0

    for (j, step) in individual:
        # assert step == job_step[j]
        machine, duration = jobs[j][step]
        start = max(machine_times[machine], job_times[j])
        end = start + duration
        machine_times[machine] = end
        job_times[j] = end
        job_step[j] += 1
        schedule.append((j, step, machine, start, end))
        makespan = max(makespan, end)

    return makespan, schedule


def selection(population, fitness, num_parents):
    """锦标赛选择"""
    selected = []
    for _ in range(num_parents):
        candidates = random.sample(list(zip(population, fitness)), 3)
        best = min(candidates, key=lambda x: x[1])[0]
        selected.append(best)
    return selected


def crossover(p1, p2):
    """顺序交叉（OX）"""
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start : end + 1] = p1[start : end + 1]
    existing = set(child[start : end + 1])
    remaining = [gene for gene in p2 if gene not in existing]
    ptr = 0
    for i in range(size):
        if child[i] is None:
            child[i] = remaining[ptr]
            ptr += 1
    return child


def mutate(individual):
    """交换不同工件的两个工序"""
    idx1, idx2 = random.sample(range(len(individual)), 2)
    if individual[idx1][0] != individual[idx2][0]:
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual


def plot_gantt(schedule):
    """绘制甘特图"""
    machines = sorted(list(set(task[2] for task in schedule)))
    fig, ax = plt.subplots(figsize=(10, 4))
    colors = plt.cm.tab10.colors
    temp = 1
    for task in schedule:
        j, _, m, start, end = task
        y = machines.index(m)
        ax.barh(
            y,
            end - start,
            left=start,
            height=0.5,
            color=colors[j % 10],
            edgecolor="black",
        )
        ax.text(
            (start + end) / 2,
            y,
            f"工件{j+1}",
            ha="center",
            va="center",
            color="white",
        )
        temp = temp + 1
    ax.set_yticks(range(len(machines)))
    ax.set_yticklabels([f"机器 {m+1}" for m in machines])
    ax.set_xlabel("时间")
    ax.set_title("甘特图")
    strmp = "最优运行时间为：" + str(makespan)
    plt.text(8, 2.5, strmp, size=26)

    plt.tight_layout()
    plt.show()


# 初始化种群
population = [create_individual(jobs) for _ in range(POP_SIZE)]
# print("pop=", population)
est_individual = None
best_makespan = float("inf")

# 主循环
plt.figure(num="最短完成时间和遗传代数关系")
pre_makespan = 0
for gen in range(NUM_GENERATIONS):
    # 评估适应度
    fitness = []
    schedules = []
    for ind in population:
        makespan, schedule = calculate_makespan(ind, jobs)
        fitness.append(makespan)
        if makespan < best_makespan:
            best_makespan = makespan
            best_individual = ind.copy()
    plt.plot([gen, gen + 1], [pre_makespan, best_makespan], lw=2, clip_on=False)
    plt.xlabel("遗传代数")
    plt.ylabel("完工时间")
    plt.title("最小完工时间和遗传代数关系")
    plt.grid(True)

    pre_makespan = best_makespan
    # 选择父代
    parents = selection(population, fitness, POP_SIZE)

    # 生成子代
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = parents[i], parents[i + 1 % POP_SIZE]
        c1, c2 = p1.copy(), p2.copy()

        if random.random() < CX_PROB:
            c1 = crossover(p1, p2)
            c2 = crossover(p2, p1)

        if random.random() < MUT_PROB:
            c1 = mutate(c1)
        if random.random() < MUT_PROB:
            c2 = mutate(c2)

        offspring.extend([c1, c2])

    population = offspring[:POP_SIZE]

# 输出结果
print(f"Best makespan: {best_makespan}")
makespan, best_schedule = calculate_makespan(best_individual, jobs)
plot_gantt(best_schedule)
