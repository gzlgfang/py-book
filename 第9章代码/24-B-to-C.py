

 首先安装必要的库（在终端中运行）
# pip install deoldify
# pip install torch torchvision
# pip install fastai==2.4.1  # 注意版本兼容性


from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *

# 设置使用CPU或GPU（如果有）
device.set(device=DeviceId.CPU)  # 改为 DeviceId.GPU 如果有NVIDIA GPU

# 初始化着色器
colorizer = get_image_colorizer(artistic=True)

# 输入和输出路径
input_path = "./black_white_image.jpg"  # 替换为你的黑白图片路径
output_path = "./colorized_image.jpg"  # 输出路径

# 渲染彩色图像（render_factor调整渲染效果，范围30-40之间效果较好）
try:
    result = colorizer.get_transformed_image(
        input_path, render_factor=35, watermarked=False
    )
    if result is not None:
        result.save(output_path)
        print(f"彩色图片已保存至 {output_path}")
        result.show()  # 在Jupyter中显示图片
    else:
        print("渲染失败，请检查输入路径")
except Exception as e:
    print(f"发生错误: {str(e)}")


from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

from deoldify.visualize import *
plt.style.use('dark_background')
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_video_colorizer()

#NOTE:  Max is 44 with 11GB video cards.  21 is a good default
render_factor=21


file_name_ext = file_name + '.mp4'
result_path = None

colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)