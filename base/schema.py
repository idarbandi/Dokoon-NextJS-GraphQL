"""
********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 ********************************************************************************
"""

# وارد کردن ماژول‌های مورد نیاز
import graphene

# وارد کردن طرح‌واره‌های ماژول‌های حساب کاربری و فروشگاه
import account.schema
import store.schema


# تعریف کلاس کوئری اصلی دکون که از کوئری‌های حساب و فروشگاه ارث‌بری می‌کنه
class DokoonQuery(store.schema.DokoonQuery, account.schema.DokoonQuery, graphene.ObjectType):
    # اینجا می‌تونیم کوئری‌های عمومی دکون رو اضافه کنیم
    pass

# تعریف کلاس Mutation اصلی دکون که از Mutation‌های حساب ارث‌بری می‌کنه


class DokoonMutation(account.schema.DokoonMutation, graphene.ObjectType):
    # اینجا می‌تونیم Mutation‌های عمومی دکون رو اضافه کنیم
    pass


# ساختن طرح‌واره گراف‌کیوال با استفاده از کوئری و Mutation دکون
schema = graphene.Schema(query=DokoonQuery, mutation=DokoonMutation)
