import yfinance as yf
import matplotlib.pyplot as plt

# Ford hisse verileri
ford = yf.Ticker("F")

# Belirtilen tarih aralığında "işlem gören günler" için veriler
data = ford.history(period="1y", start="2023-01-01", end="2023-12-31")

# NaN verileri atmak ve tekrarlanan satırları kaldırmak için
data = data.dropna(subset=['Close']).drop_duplicates()

# Verilerin boş olup olmadığının kontrolü
if data.empty:
    print("Veri bulunamadı!")
else:
    # Kapanış fiyatlarının grafiği
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], color='blue')
    plt.title('Ford - F - 2023')
    plt.ylabel('Kapanış Fiyatı (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
