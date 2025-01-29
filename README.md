# โปรเจคดึงข้อมูล Google Search Console API ด้วย Python Flask

โปรเจคนี้จะเป็นการดึงและแสดงผลข้อมูลจาก Google Search Console API ได้ โดยรวมการยืนยันตัวตนผ่าน OAuth, การดึงข้อมูล และหน้าเว็บสำหรับแสดงผลการวิเคราะห์ข้อมูลที่ได้

## Requirements

- Python 3.8 หรือสูงกว่า
- บัญชี Google Cloud Console
- สิทธิ์การเข้าถึง Google Search Console
- ไฟล์ `credentials.json` จาก Google Cloud Console

## โครงสร้างโปรเจค

```
gsc-api/
├── auth/                  
│   ├── __init__.py
│   └── google_auth.py
├── api/                  
│   ├── __init__.py
│   └── search_console.py
├── utils/                
│   ├── __init__.py
│   └── file_utils.py
├── templates/            
│   └── dashboard.html
├── static/              
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── main.py               
├── app.py                
├── requirements.txt
├── credentials.json      
└── token.json
```

## การติดตั้ง

1. Clone โปรเจค:

```bash
git clone https://github.com/son-content-mastery/google-search-console-api-fetch.git
cd gsc-api
```

2. สร้างและเปิดใช้งาน virtual environment:

```bash
# สำหรับ Windows
python -m venv venv
venv\Scripts\activate

# สำหรับ macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. ติดตั้งแพ็คเกจที่จำเป็น:

```bash
pip install -r requirements.txt
```

## การตั้งค่า

1. วางไฟล์ `credentials.json` (ที่ได้จาก Google Cloud Console) ไว้ในโฟลเดอร์หลักของโปรเจค

2. แก้ไข URL ของเว็บไซต์ใน `main.py`:
#### สำหรับ Domain Property 
site_url = 'sc-domain:yourwebsite.com'  # ไม่ต้องใส่ https:// หรือ www

#### สำหรับ URL-prefix Property
site_url = 'https://www.yourwebsite.com/'  # ต้องมี protocol (https://) และต้องมี / ต่อท้าย

## วิธีการใช้งาน

1. รันสคริปต์ดึงข้อมูลก่อน:

```bash
python main.py
```

สคริปต์นี้จะ:
- ยืนยันตัวตนกับ Google Search Console API
- สร้างไฟล์ `token.json` (ถ้ายังไม่มี)
- ดึงข้อมูลการวิเคราะห์การค้นหา
- บันทึกข้อมูลเป็นไฟล์ CSV

2. เริ่มต้นแอปพลิเคชัน Flask:

```bash
python app.py
```

แอปพลิเคชันจะทำงานที่ `http://localhost:5000`

## แพ็คเกจที่จำเป็น

แพ็คเกจหรือไลบรารีต่อไปนี้จะถูกติดตั้งผ่าน `requirements.txt`:

```
flask==2.0.1
google-auth==2.3.3
google-auth-oauthlib==0.4.6
google-auth-httplib2==0.1.0
google-api-python-client==2.31.0
pandas==1.3.3
```

## การแก้ไขปัญหา

1. กรณีพบปัญหาเกี่ยวกับ OAuth:
   - ตรวจสอบว่าไฟล์ `credentials.json` อยู่ในตำแหน่งที่ถูกต้อง
   - ตรวจสอบการตั้งค่าหน้า OAuth consent screen
   - ตรวจสอบว่าได้เปิดใช้งาน Google Search Console API ใน Google Cloud Console แล้ว

2. กรณีข้อมูลไม่แสดงผล:
   - ตรวจสอบว่าไฟล์ `search_analytics.csv` ถูกสร้างโดย `main.py` แล้ว
   - ตรวจสอบว่า URL ของเว็บไซต์ในไฟล์ `main.py` ถูกต้อง
   - ตรวจสอบว่าคุณมีสิทธิ์ใน Google Search Console หรือไม่


## รีซอร์สเพิ่มเติม
- [ทำความรู้จัก Flask เว็บเฟรมเวิร์คสุดง่าย เขียนสนุกของภาษา Python](https://devhub.in.th/blog/flask-python)
- [ทำความเข้าใจ Virtual Environment สิ่งที่คนเขียน Python ต้องรู้](https://devhub.in.th/blog/python-virtual-environment-venv)

