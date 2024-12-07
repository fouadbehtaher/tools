import os
import requests
import json

class UpdateNotifier:
    def __init__(self, current_version, update_url):
        self.current_version = current_version
        self.update_url = update_url

    def check_for_updates(self):
        """
        يتحقق من التحديثات المتوفرة عبر الاتصال بمصدر خارجي (مثال: خدمة ويب توفر آخر التحديثات)
        """
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
        """
        يقارن بين الإصدار الحالي والإصدار الأخير المتوفر
        """
        return latest_version > self.current_version

    def notify_user(self, latest_version):
        """
        يقوم بتنبيه المستخدم عند توفر تحديث جديد
        """
        print(f"تحديث جديد متوفر! الإصدار الجديد هو {latest_version}.")
        print("يرجى تحديث الأداة للحصول على الميزات الجديدة والتحسينات.")

    def update_tool(self):
        """
        يقوم بتحديث الأداة إلى أحدث إصدار عبر عملية التحميل أو النسخ.
        """
        print("يتم تحديث الأداة...")  # يتم تحميل التحديثات هنا إذا كانت هناك آلية لذلك
        
        
        
        print("تم التحديث بنجاح!")


if __name__ == "__main__":
    current_version = "1.0.0"  
    update_url = "https://your-update-server.com/api/check_for_updates"  

    notifier = UpdateNotifier(current_version, update_url)
    notifier.check_for_updates()  
