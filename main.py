import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant

# تنظیمات اصلی
API_ID = 34996139
API_HASH = "a1f3db16cae2919cfb05e61d1e968b8d"
OWNER_ID = 7993567805

# سشن استرینگ شما
SESSION_STRING = "1BJWap1sBu53LB1uFP0WTdUjJDJQDCy4SRMvGUY-Tq8N4noeYndwg2jkrk1lHwPeFKR2VfpBfZYvIycwi9VMuxDKHwPgNe74fyGU18279ENyfgs17iHQWtsFsxkoT2VJvW-w7y5iJxZqbFe4gKlSSVJs1SCZKDmFHqg9_GQd8Bq2mTgrn6xse862nAuSlSXmhf14GKEgHJVYOIBgBuFBCNp2wfxJx1EZMtV9tAIWaeEzGID2YUdx20Kq2rju5PUoNk5H5_r4QFEAn5UeM1OO6Puq-it4SCKlcKhOd3rOrcu_ZFE9i96sUweAWsFfVclF_CbZwoZHg8tp-fvbxWqViUGYnI9sxYt4="

# کانال و گروه جوین اجباری
REQUIRED_CHANNEL = "selfqmeiwe"
REQUIRED_GROUP = "selfqmeiw"

user_balances = {}

# راه‌‌اندازی کلاینت پایروگرام
app = Client(
    "my_selfbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# تابع بررسی عضویت اجباری
async def check_membership(client: Client, user_id: int):
    if user_id == OWNER_ID:
        return True
    try:
        await client.get_chat_member(REQUIRED_CHANNEL, user_id)
        await client.get_chat_member(REQUIRED_GROUP, user_id)
        return True
    except UserNotParticipant:
        return False
    except Exception:
        return True

# هندلر برای دستور .panel یا کلمه فارسی پنل در هر چتی
@app.on_message(filters.command(["panel"], prefixes=".") | filters.regex(r"^پنل$"))
async def panel_command(client: Client, message: Message):
    user_id = message.from_user.id
    
    # بررسی عضویت
    if not await check_membership(client, user_id):
        join_text = (
            "⚠️ **برای استفاده از ربات، ابتدا باید در کانال و گروه زیر عضو شوید:**\n\n"
            f"📢 کانال: https://t.me/{REQUIRED_CHANNEL}\n"
            f"👥 گروه: https://t.me/{REQUIRED_GROUP}\n\n"
            "پس از عضویت، دوباره کلمه «پنل» یا دستور `.panel` را بفرستید."
        )
        return await message.edit_text(join_text)

    # متن پنل مدیریتی
    panel_text = (
        "🎛 **پنل مدیریت پیشرفته سلف‌بات** 🎛\n\n"
        "🔹 مدیریت حساب، پروفایل و ابزارهای حرفه‌ای\n"
        "🔹 سیستم موجودی الماس و بازی‌ها\n"
        "🔹 ابزارهای مدیریتی و ادمینی گروه\n\n"
        f"💎 **موجودی شما:** {user_balances.get(user_id, 0)}"
    )
    await message.edit_text(panel_text)

print("سلف‌بات با موفقیت اجرا شد...")
app.run()
