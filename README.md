
# 📝 TODO Reminder App

A simple Python desktop application to manage tasks with time-based reminders. Built using `tkinter` for the UI and `plyer` for desktop notifications.

Created by **Zohaire Ahmed**.

---

## 📦 Features

- ⏰ **Add Tasks with Time** – Schedule reminders using HH:MM format.
- 🔔 **Get Notified** – Automatic pop-up notifications at the exact time.
- 🧹 **Delete Tasks** – Easily remove unwanted tasks.
- 🕒 **Live Clock** – Displays the current time.
- 🎨 **Minimal UI** – Clean and simple task manager interface.

---

## 🖼️ GUI Preview
![APP SS](https://media.discordapp.net/attachments/1265694796308283515/1362898513138159716/image.png?ex=680411a6&is=6802c026&hm=38b5b2127bb340e7ee55def705597ccf0949ee36c7ff279d1a156ed54d01bef8&=&format=webp&quality=lossless&width=482&height=325)
![Color Selection](https://media.discordapp.net/attachments/1265694796308283515/1362898562211381479/image.png?ex=680411b2&is=6802c032&hm=328893e799ee9839edaef351165ee6abf88190ed0819c77f33888e2e0b145857&=&format=webp&quality=lossless&width=469&height=372)
![Board Prew](https://media.discordapp.net/attachments/1265694796308283515/1362898561972437182/image.png?ex=680411b2&is=6802c032&hm=7c4d08ceadc4d7161d62ecdc89462106fb54f6c27e891655107be5f759ad8859&=&format=webp&quality=lossless&width=966&height=521)
---

## 📁 File Structure

```
todo-reminder-app/
├── main.py           # Main application UI and logic
├── notify.py         # Notification handler using plyer
├── icon.ico          # Icon for the app window and notifications
├── README.md         # Project documentation
```

---

## 🚀 Getting Started

### ✅ Requirements

Install required Python libraries (if you don’t already have them):

```bash
pip install plyer
```

### ▶️ Run the App

```bash
python main.py
```

---

## 💡 How It Works

- Add a task and specify the reminder time in `HH:MM` format.
- The app checks every 30 seconds if any task matches the current time.
- If matched, a desktop notification appears, and the task is removed from the list.

---

## ⚙️ Example

1. Enter:  
   - Task: `Attend meeting`  
   - Time: `14:30`
2. Click **Add Task**.
3. At 2:30 PM, you’ll get a notification:  
   📢 _"Reminder: Attend meeting"_

---

## 🧠 Tips & Notes

- Time must be in **24-hour format** → e.g., `09:00`, `15:45`.
- The app icon (`icon.ico`) is used for window and notifications.
- Make sure the `notify.py` is in the same folder as `main.py`.

---

## 🛑 Known Issues

- Tasks are only checked every 30 seconds; exact-to-the-second reminders are not guaranteed.
- The app must stay open to receive notifications.
- No support for recurring tasks yet.

---

## 🧰 Future Improvements

- [ ] Save tasks to a file for persistence after app restarts.
- [ ] Add recurring reminders.
- [ ] GUI enhancements using `customtkinter` or `ttkbootstrap`.

---

## 🙌 Credits

- **Developer**: Zohair Ahmed Nadeem 
- **Notification**: [Plyer](https://plyer.readthedocs.io/en/latest/)

---

## 📜 License

This project is licensed under the MIT License.

---
