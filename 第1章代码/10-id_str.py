old_str = "123456789"
new_str1 = old_str[3:6]  # 从第4个字符开始截取到第6个字符位置，间隔1
new_str2 = old_str[5:8:2]  # 从第6个字符开始截取到第8个字符位置，间隔2
new_str3 = old_str[2:]  # 从第3个字符开始截取到最后一个字符，间隔1
new_str4 = old_str[4:-2]  # 从第5个字符开始截取到倒数第3个字符，间隔1
print("new_str1=", new_str1, "       new_str2=", new_str2)
print("new_str2=", new_str3, "   new_str4=", new_str4)
