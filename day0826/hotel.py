file_path = './day0826/hotel.txt'

print('---- 호텔 라디 ----')

rooms = []

for floor in range(1,4):                    #리스트 형식으로 소개 만들어보기 
    for num in range(1,4):
        room_number = f"{floor}0{num}"
        rooms.append(room_number)
        print(room_number, end='\t')
    print()
  
         
while True:    
    print()
    print("[1] 조회  [2] 입실  [3] 퇴실  [0] 종료")  

    try:                                        # 자바에서 트라이~캐치로 오류잡았떤게 여기서는 트라이~익셉트다! 기억기억
        choice = int(input(" 번호를 선택해 주세요 🙂 : "))
    except ValueError:
        print()
        print("❌ 숫자만 입력이 가능합니다~")
        continue
    if choice == 0:
        print()
        print("관리 프로그램을 종료합니다.")
        break
    elif choice == 1:      ## 조회
        print("===조회===\n")
        with open(file_path, 'r',encoding='utf-8') as f:
            lines = f.readlines()
        checkin = {}  # 키:값 형태이므로 딕셔너리 
        for line in lines:
            name, room = line.strip().split(",")
            checkin[room] = name  # hotel.txt에 있던 기록을 딕셔너리로 옮겨 담는 과정  룸을 검색해서 이름을 저장한다 이런느낌 

        for floor in range(1,4):
            for num in range(1,4):
                room_number = f"{floor}0{num}"
                rooms.append(room_number)      #룸즈에다가 룸넘버를 맨뒤에 집어넣는다 어팬드!
                print(room_number, end='\t')
            print()

            for num in range(1,4):
                room_number = f"{floor}0{num}"
                if room_number in checkin:  # 딕셔너리에 방번호가 있으면 (= 입실자 있음)
                    print(checkin[room_number], end='\t')   # 여기는 읽어오는 느낌인거지 룸넘버를 검색하면 이름이나오는거지 
                else:
                    print("---", end='\t')       # 없으면 ---
            print()                   
            

    elif choice == 2:   ## 입실
        print()    
        print("===체크인===\n")
        name = input("이름을 입력하세요: ")        
        while True: #자꾸 틀리면 처음부터 시작해서 방번호만 다시묻게 
            print()
            room = input("방번호를 입력하세요: ")

            if room not in rooms: # 방 존재여부 확인하기
                print("❌ 없는 객실입니다. 101호~303호 사이만 가능합니다.\n")
                continue
            with open(file_path, 'r', encoding ='utf-8')as f:  # 이미 사용중인 방 거르기
                lines = f.readlines()
            used_rooms = [line.strip().split(",")[1] for line in lines]
            
            if room in used_rooms:
                print(f"❌ {room}호는 이미 사용중입니다.\n")
                continue           
            break    
                
        print(f"{room}호 선택\n" )   

        with open(file_path, 'a', encoding='utf-8') as f:  #txt에 입실정보 추가하기?
            f.write(name + "," + room + '\n')
        print(f"{name}님 {room}호 입실 완료!\n") 
        

    elif choice == 3:   ##퇴실
        print("===체크아웃==\n")
        room = input("퇴실할 방번호를 입력하세요 : ")

        with open(file_path, 'r', encoding = 'utf-8') as f:   
            lines = f.readlines()
        
        
        new_lines = []
        found = False

        for line in lines:
            name, r = line.strip().split(",")   
            if r == room:                                       # 만약 퇴실할 방번호면?
                print(f"{name}님 {room}호 퇴실 완료!\n")         
                found = True                                    # 그냥 끝 
            else:
                new_lines.append(line)                          # 나머지방은 뉴라인스에 어펜드 

        if not found:
            print(f"❌ {room}호에는 입실자가 없습니다.\n") 

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)       #뉴라인즈는 여러줄 갖고있기 때문에 그냥 write하면 에러터진대     

    else:
        print()
        print("❌ 잘못된 입력입니다 0, 1, 2, 3 으로 입력해주세요.")   
              







