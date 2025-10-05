# ===============================
# 🎨 Simple Plot in Python
# ===============================

import matplotlib.pyplot as plt
import numpy as np

# إنشاء بيانات (مثلاً time و voltage)
x = np.linspace(0, 10, 100)   # 100 نقطة من 0 إلى 10
y = np.sin(x)                 # نرسم دالة sin كمثال

# رسم البيانات
plt.figure(figsize=(8,5))     # حجم الشكل
plt.plot(x, y, label='Sine Wave', color='b', linewidth=2)

# إضافة عناوين
plt.title("Sine Wave Example")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# إظهار شبكة صغيرة للمساعدة في القراءة
plt.grid(True, linestyle='--', alpha=0.7)

# إظهار وسيلة الإيضاح (legend)
plt.legend()

# عرض الرسم
plt.show()
