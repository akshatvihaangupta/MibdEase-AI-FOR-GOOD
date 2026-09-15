# ============================================================
#   MENTAL HEALTH CHECK-IN PORTAL  (Single File, No Backend)
#   File: project.py
#   Run : python project.py
# ============================================================

import json
import os
from datetime import datetime

# ---------- FILE PATHS ----------
ALERT_LOG   = "admin_alerts.log"
STUDENT_DB  = "students.json"

# ============================================================
#   ADMIN ALERT FUNCTION (simulated server)
# ============================================================
def send_alert_to_admin(student_data, status, score, reasons):
    alert = {
        "type": "MENTAL_HEALTH_ALERT",
        "status": status,
        "risk_score": score,
        "reg_no": student_data.get("reg_no", "N/A"),
        "college_name": student_data.get("college_name", "N/A"),
        "student": student_data["name"],
        "mood": student_data["mood"],
        "day_rating": student_data["day_rating"],
        "last_CA_%": student_data["ca"],
        "sleep_hours": student_data["sleep"],
        "sleep_time": student_data["sleep_time"],
        "lonely": student_data["lonely"],
        "emotion": student_data["emotion"],
        "reason": student_data.get("reason", ""),
        "reasons": reasons,
        "timestamp": datetime.now().isoformat()
    }

    print("\n" + "=" * 60)
    print("🚨 ALERT SENT TO ADMIN SERVER 🚨")
    print("=" * 60)
    print(json.dumps(alert, indent=2))
    print("=" * 60)

    try:
        with open(ALERT_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(alert) + "\n")
        print(f"✅ Alert saved to {ALERT_LOG}")
    except Exception as e:
        print("❌ Could not save alert log:", e)


# ============================================================
#   SCORING LOGIC (rule-based — NOT a diagnosis)
# ============================================================
def evaluate_student(data):
    score = 0
    reasons = []

    # Mood
    if data["mood"] <= 3:
        score += 2
        reasons.append("very low mood")
    elif data["mood"] <= 5:
        score += 1
        reasons.append("low mood")

    # Day rating
    if data["day_rating"] in ("Very Bad", "Bad"):
        score += 1
        reasons.append(f"day was {data['day_rating'].lower()}")

    # Last CA score
    if data["ca"] < 40:
        score += 2
        reasons.append("very poor recent CA score")
    elif data["ca"] < 60:
        score += 1
        reasons.append("declining CA score")

    # Sleep hours
    if data["sleep"] < 5:
        score += 1
        reasons.append("insufficient sleep")

    # Loneliness
    if data["lonely"]:
        score += 1
        reasons.append("reports feeling lonely")

    # Negative emotion
    if data["emotion"] in ("Sad", "Angry", "Anxious", "Tired", "Lonely"):
        score += 1
        reasons.append(f"feeling {data['emotion'].lower()}")

    # Decide status
    if score >= 4:
        status = "HIGH_CONCERN"
    elif score >= 2:
        status = "MODERATE_CONCERN"
    else:
        status = "OK"

    return status, score, reasons


# ============================================================
#   INPUT HELPERS
# ============================================================
def get_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")


def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("yes", "y"):
            return True
        if ans in ("no", "n"):
            return False
        print("⚠️  Please answer 'yes' or 'no'.")


def get_choice(prompt, options):
    """Show numbered options, return the chosen string."""
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"   {i}. {opt}")
    while True:
        try:
            idx = int(input("Enter choice number: ").strip())
            if 1 <= idx <= len(options):
                return options[idx - 1]
            print(f"⚠️  Please choose between 1 and {len(options)}.")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")


# ============================================================
#   STUDENT CHECK-IN
# ============================================================
def collect_feedback(reg_no, college_name):
    print("\n" + "=" * 60)
    print("       MENTAL HEALTH CHECK-IN PORTAL  (Student)")
    print("=" * 60)
    print("This is a wellbeing check — NOT a medical diagnosis.")
    print("If you are in crisis, call Tele-Nexus: 14001 (India)\n")

    print(f"Registration Number: {reg_no}")
    print(f"College/School/University: {college_name}\n")

    name = input("Your name: ").strip() or "Anonymous"

    mood = get_int("Today's mood rating (1 = very sad, 10 = very happy): ", 1, 10)

    day_rating = get_choice(
        "\nHow was your day?",
        ["Very Good", "Good", "Okay", "Bad", "Very Bad"]
    )

    sleep = get_int("\nHours of sleep last night: ", 0, 24)

    sleep_time = input("What time did you sleep last night? (e.g. 11:30 PM): ").strip() or "Not mentioned"

    lonely = get_yes_no("\nAre you feeling lonely? (yes/no): ")

    ca = get_int("\nYour last CA / exam score (%): ", 0, 100)

    # Emotion question (Hinglish)
    emotion = get_choice(
        "\nAaj aapko sabse zyada kaunsa emotion feel ho raha hai?",
        ["Happy", "Sad", "Angry", "Anxious", "Tired", "Lonely", "Excited", "Calm", "Confused"]
    )

    # Reason question — OPTIONAL, only if user is NOT happy
    reason = ""
    if emotion.lower() != "happy" and mood <= 6:
        reason = input(
            "\nAaj aapke mood ke peeche sabse badi wajah kya hai? "
            "(optional — press Enter to skip)\n> "
        ).strip()
        if reason == "":
            reason = "Not mentioned"

    return {
        "reg_no": reg_no,
        "college_name": college_name,
        "name": name,
        "mood": mood,
        "day_rating": day_rating,
        "sleep": sleep,
        "sleep_time": sleep_time,
        "lonely": lonely,
        "ca": ca,
        "emotion": emotion,
        "reason": reason,
        "time": datetime.now().isoformat()
    }


# ============================================================
#   SAVE STUDENT RECORD
# ============================================================
def save_student_record(data, status, score):
    record = {**data, "status": status, "risk_score": score}

    existing = []
    if os.path.exists(STUDENT_DB):
        try:
            with open(STUDENT_DB, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = []

    existing.append(record)

    with open(STUDENT_DB, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)


# ============================================================
#   STUDENT INTERFACE
# ============================================================
def student_interface(reg_no, college_name):
    while True:
        data = collect_feedback(reg_no, college_name)
        status, score, reasons = evaluate_student(data)

        save_student_record(data, status, score)

        print("\n" + "-" * 60)
        print(f"Result for {data['name']} ({reg_no}): {status} (risk score = {score})")
        if reasons:
            print("Signals noticed: " + ", ".join(reasons))
        else:
            print("No concerning signals detected. Keep it up! 💪")

        if status == "HIGH_CONCERN":
            print("\n💙 We care about you. Please consider talking to a counselor.")
            print("   iCall: 91XXXXXX21 | NEXUS: 98XXXXXX26 | Tele-Nexus: 14001")
            send_alert_to_admin(data, status, score, reasons)
        elif status == "MODERATE_CONCERN":
            print("\n💛 Take care of yourself. A short chat with a friend may help.")
            send_alert_to_admin(data, status, score, reasons)

        print("-" * 60)

        again = get_yes_no("\nCheck in another student? (yes/no): ")
        if not again:
            print("\nReturning to main menu...\n")
            break

        # ✅ ASK FOR NEW REGISTRATION NUMBER AND COLLEGE NAME FOR NEXT STUDENT
        reg_no = input("ENTER YOUR COLLEGE/SCHOOL/UNIVERSITY REGISTRATION NUMBER: ").strip()
        if reg_no == "":
            reg_no = "Anonymous"
        college_name = input("ENTER YOUR SCHOOL/COLLEGE/UNIVERSITY NAME: ").strip()
        if college_name == "":
            college_name = "Not mentioned"


# ============================================================
#   ADMIN INTERFACE
# ============================================================
def admin_interface():
    print("\n" + "=" * 60)
    print("            ADMIN DASHBOARD")
    print("=" * 60)

    if not os.path.exists(STUDENT_DB):
        print("⚠️  No student records found yet.")
        input("\nPress Enter to return to main menu...")
        return

    try:
        with open(STUDENT_DB, "r", encoding="utf-8") as f:
            records = json.load(f)
    except Exception as e:
        print("❌ Could not read student database:", e)
        input("\nPress Enter to return to main menu...")
        return

    if not records:
        print("No records to display.")
        input("\nPress Enter to return to main menu...")
        return

    print(f"\nTotal check-ins: {len(records)}\n")

    # Summary counts
    high = sum(1 for r in records if r.get("status") == "HIGH_CONCERN")
    mod  = sum(1 for r in records if r.get("status") == "MODERATE_CONCERN")
    ok   = sum(1 for r in records if r.get("status") == "OK")

    print(f"🔴 HIGH_CONCERN     : {high}")
    print(f"🟡 MODERATE_CONCERN : {mod}")
    print(f"🟢 OK               : {ok}")
    print("-" * 60)

    # Show only concerning students in detail
    for i, r in enumerate(records, 1):
        if r.get("status") == "OK":
            continue
        print(f"\n#{i}  {r.get('name', 'Anonymous')}  |  {r.get('status')}  (score={r.get('risk_score')})")
        print(f"   Reg No       : {r.get('reg_no', 'N/A')}")
        print(f"   College Name : {r.get('college_name', 'N/A')}")
        print(f"   Mood         : {r.get('mood')}/10")
        print(f"   Day          : {r.get('day_rating')}")
        print(f"   Emotion      : {r.get('emotion')}")
        print(f"   Sleep        : {r.get('sleep')} hrs  (slept at {r.get('sleep_time')})")
        print(f"   Lonely       : {r.get('lonely')}")
        print(f"   Last CA      : {r.get('ca')}%")
        if r.get("reason"):
            print(f"   Reason (why) : {r.get('reason')}")
        print(f"   Time         : {r.get('time')}")

    # Option to view ALL records
    show_all = get_yes_no("\nShow ALL records (including OK)? (yes/no): ")
    if show_all:
        print("\n" + "-" * 60)
        for i, r in enumerate(records, 1):
            print(f"\n#{i}  {r.get('name')}  |  {r.get('status')}  (score={r.get('risk_score')})")
            print(f"   Reg No       = {r.get('reg_no', 'N/A')}")
            print(f"   College Name = {r.get('college_name', 'N/A')}")
            print(f"   Mood={r.get('mood')}  Day={r.get('day_rating')}  Emotion={r.get('emotion')}")
            print(f"   Sleep={r.get('sleep')}h  Time={r.get('sleep_time')}  Lonely={r.get('lonely')}")
            print(f"   CA={r.get('ca')}%  Reason={r.get('reason') or '-'}")

    # Show alert log if exists
    if os.path.exists(ALERT_LOG):
        view_alerts = get_yes_no("\nView admin_alerts.log? (yes/no): ")
        if view_alerts:
            print("\n" + "=" * 60)
            print("           ADMIN ALERTS LOG")
            print("=" * 60)
            try:
                with open(ALERT_LOG, "r", encoding="utf-8") as f:
                    for line in f:
                        print(line.rstrip())
            except Exception as e:
                print("❌ Could not read alert log:", e)

    input("\nPress Enter to return to main menu...")


# ============================================================
#   MAIN MENU (Two Interfaces)
# ============================================================
def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("        MENTAL HEALTH CHECK-IN PORTAL")
        print("=" * 60)
        print("   1. Student Check-in")
        print("   2. Admin Dashboard")
        print("   3. Exit")
        print("=" * 60)

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            aaa = input("ENTER YOUR COLLEGE/SCHOOL/UNIVERSITY REGISTRATION NUMBER: ").strip()
            if aaa == "":
                aaa = "Anonymous"
            # ✅ COLLEGE NAME JUST AFTER REGISTRATION NUMBER
            college = input("ENTER YOUR SCHOOL/COLLEGE/UNIVERSITY NAME: ").strip()
            if college == "":
                college = "Not mentioned"
            student_interface(aaa, college)

        elif choice == "2":
            passw = input("PASSWORD: ")
            if passw == "CARS":
                admin_interface()
            else:
                print("WRONG PASSWORD - TRY AGAIN")
                passw = input("AGAIN ENTER THE PASSWORD: ")
                if passw == "CARS":
                    admin_interface()
                else:
                    print("AGAIN WRONG PASSWORD")
                    print("Thank you")

        elif choice == "3":
            print("\nGoodbye! Take care. 💙")
            break
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, or 3.")


# ============================================================
#   ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main_menu()