import time 
print("-"*10,"⌛ welcome to pomodoro app".title(),"-"*10)
while True:
    try:
        minutes = int(input("⌚ Enter time in minutes: ".title()))

        if minutes<1:
            print("❌ must be more than zero.".title())
            continue
        # تحويل الدقائق لثوانى ليسهل التعامل معاها
        seconds = minutes*60
        while seconds>-1:
            # كم دقيقة فى الرقم المدخل
            minute = seconds//60
            # الثوانى المتبقية اى باقى الرقم العشرى
            second = seconds%60

            seconds-=1

            print(f"\r⏱️  remaining time: {minute:02d}:{second:02d}".title(),end="")
            time.sleep(1)
        if second==0:
            break
    except ValueError:
        print("❌ invalid value! must be integer.".title())

print("\n\n⏰ Time's Up Take a Break.")
input("click enter to end program. ".title())

# minutes=1.5
# print(f"minutes: {minutes}")

# seconds=minutes*60
# print(f"seconds: {seconds}")

# minute=seconds//60
# print(f"minute: {minute}")

# second=seconds%60
# print(f"second: {second}")