import matplotlib.pyplot as plt

# بيانات نموذجية
categories = ['الطعام', 'الإيجار', 'النقل', 'أخرى']
expenses = [300, 600, 150, 250]

# إنشاء مخطط دائري
plt.pie(expenses, labels=categories, autopct='%1.1f%%')

# العنوان
plt.title("النفقات الشهرية")

plt.show()