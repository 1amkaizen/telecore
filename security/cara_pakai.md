### ✅ Cara Pemakaian di Handler

```python
from core_bot.security.admin import is_admin

if not is_admin(update.effective_user.id):
    await update.message.reply_text("❌ Kamu tidak punya akses admin.")
    return
```

---

### ✅ .env Contoh

```env
ADMIN_ID=123456789,987654321
```

---

### ✅ Bonus (Opsional Decorator)

Kalau nanti kamu mau pakai decorator (contoh di `telegram.ext`):

```python
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from core_bot.security.admin import is_admin

def admin_only(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if not is_admin(user_id):
            await update.message.reply_text("❌ Akses hanya untuk admin.")
            return
        return await func(update, context)
    return wrapper
```

