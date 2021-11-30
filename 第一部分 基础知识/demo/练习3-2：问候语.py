"""
继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每
人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
"""
names = ['jasmine', 'tom', 'alis']
message = f"Hello,{names[0].title()}"
print(message)
# ...