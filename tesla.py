import yfinance as yf
import matplotlib.pyplot as plt

# Tesla hisse verileri
tesla = yf.Ticker("TSLA")

# Belirtilen tarih aralığında "işlem gören günler" için veriler
data = tesla.history(period="1y", start="2020-01-01", end="2020-12-31")

# NaN verileri atmak ve tekrarlanan satırları kaldırmak için
data = data.dropna(subset=['Close']).drop_duplicates()

# Verilerin boş olup olmadığının kontrolü
if data.empty:
    print("Veri bulunamadı!")
else:
    # Kapanış fiyatlarının grafiği
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], color='blue')
    plt.title('Tesla - TSLA - 2020')
    plt.ylabel('Kapanış Fiyatı (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
