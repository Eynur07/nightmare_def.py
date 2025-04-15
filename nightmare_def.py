# 🌙 Nightnmare Defender (Eynur Protokolu)
# Xəqaninin ruhu bu kodda yaşayır

def eye_squeeze():
    """Gözlərini sıxmaqla kabusu dayandırmaq"""
    print("⚠️Kabus aşkarlandı ! Gözləri 3 saniyə sıx...")
    import time
    time.sleep(3)
    print("✅Uğurlu! Yuxuya davam et.")

def breathing_378():
    """3-7-8 nəfəs alqoritmi"""
    print("\n🌬️ 3 saniyə dərin nəfəs al...")
    print("\n⏳ 7 saniyə nəfəsi tut...")
    print("\n😮‍💨 8 saniyəyə yavaşca burax...")
  
def reality_check():
    """Şüur yoxlaması"""
    answer = input("\n🤔 ətrafında saat var? (Baxmaq üçün 5 saniyə verilir): ")
    if answer.lower() == "hə":
    print("🎉Bu yuxudur! Nəzarəti ələ al.")
    else:
      print("Yenə yoxla")

if __name__ == "__main__":
    print("\n" +"Xəqani protokolu aktiv" + "\n" + "-"*30)
    eye_squeeze()
    breathing_378()
    reality_check()
