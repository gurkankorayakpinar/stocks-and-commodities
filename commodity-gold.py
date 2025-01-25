import yfinance as yf
import matplotlib.pyplot as plt

# Yahoo Finance - Altın ons sembolü: 'GC=F'
symbol = 'GC=F'

# Grafiğin başlangıç ve bitiş tarihleri
end_date = '2025-01-23'
start_date = '2020-01-23'

# Veriyi Yahoo Finance'ten indir
data = yf.download(symbol, start=start_date, end=end_date)

# Kapanış fiyatlarının grafiği
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], color='gold')
plt.title('Altın - Ons - Son 5 Yıl', fontsize=14)
plt.ylabel('Fiyat (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
