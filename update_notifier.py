import requests

class UpdateNotifier:
    def __init__(self, current_version, update_url):
        self.current_version = current_version
        self.update_url = update_url

    def check_for_updates(self):

        try:
            response = requests.get(self.update_url)
            if response.status_code == 200:
                data = response.json()
                latest_version = data.get("latest_version")
                if self.is_new_version_available(latest_version):
                    self.notify_user(latest_version)
                else:
                    print("أنت تستخدم أحدث إصدار.")
            else:
                print("حدث خطأ في الاتصال بسيرفر التحديثات.")
        except Exception as e:
            print(f"تعذر الاتصال بالخادم: {e}")

    def is_new_version_available(self, latest_version):

        return latest_version > self.current_version

    def notify_user(self, latest_version):

        print(f"تحديث جديد متوفر! الإصدار الجديد هو {latest_version}.")
        print("يرجى تحديث الأداة للحصول على الميزات الجديدة والتحسينات.")

    def update_tool(self):

        print("يتم تحديث الأداة...")  # يمكن إضافة خطوات لتحميل التحديثات هنا
        print("تم التحديث بنجاح!")
