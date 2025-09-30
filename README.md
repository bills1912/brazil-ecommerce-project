# 🛒 Brazilian E-Commerce (Olist) Data Analysis Project

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io)

Proyek analisis data komprehensif menggunakan dataset Brazilian E-Commerce dari Olist. Proyek ini mencakup analisis mendalam tentang pola penjualan, segmentasi pelanggan, analisis geografis, dan performa pengiriman dengan dashboard interaktif.

## 📊 Demo Dashboard

![Dashboard Overview](https://img.shields.io/badge/Dashboard-Live-success)

Dashboard interaktif dengan 7 halaman analisis:
- 📊 Overview - KPI dan metrik utama
- 📈 Sales Analysis - Tren dan pola penjualan
- 🗺️ Geographic Analysis - Distribusi geografis dengan heatmap
- 👥 Customer Analysis - Perilaku dan segmentasi pelanggan
- 🚚 Delivery Performance - Analisis performa pengiriman
- 🎯 RFM Segmentation - Segmentasi pelanggan RFM & Manual Clustering
- 🔗 Cross-Selling - Peluang cross-selling produk

## 🎯 Fitur Utama

### 1. **Analisis Data Lengkap (Python Script)**
✅ **Data Wrangling**
- Gathering data dari 9 dataset berbeda
- Assessing data untuk SEMUA variabel (lengkap)
- Cleaning data dengan metode yang tepat untuk setiap dataset

✅ **Exploratory Data Analysis (EDA)**
- Analisis tren penjualan dari waktu ke waktu
- Distribusi kategori produk
- Pola pembelian berdasarkan waktu
- Analisis harga dan revenue

✅ **Analisis Lanjutan (Tanpa Machine Learning)**
- **RFM Analysis**: Segmentasi pelanggan (Recency, Frequency, Monetary)
- **Geospatial Analysis**: Distribusi geografis dengan heatmap interaktif
- **Manual Clustering**: Customer grouping menggunakan binning method
- **Product Association**: Analisis cross-selling opportunities
- **Delivery Performance**: Analisis waktu dan ketepatan pengiriman

### 2. **Dashboard Interaktif (Streamlit)**
🎨 **7 Halaman Analisis**
- Interactive charts dengan Plotly
- Geographic heatmap dengan Folium
- Filter dan visualisasi dinamis
- Export-ready insights

### 3. **Visualisasi Komprehensif**
📈 **13+ Jenis Visualisasi**
- Bar charts, Pie charts, Line graphs
- Box plots, Histograms, Scatter plots
- 3D scatter plots untuk RFM
- Treemap untuk geographic data
- Interactive heatmap untuk customer distribution

## 🚀 Cara Menggunakan

### Prerequisites
```bash
# Requirements
- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Kaggle account (untuk download dataset)
```

### Quick Start

#### 1️⃣ Setup Environment

```bash
# Clone repository
git clone <repository-url>
cd olist-ecommerce-analysis

# Buat virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2️⃣ Setup Kaggle API

1. Login ke [Kaggle](https://www.kaggle.com)
2. Pergi ke **Account** → **API** → **Create New Token**
3. Download file `kaggle.json`
4. Tempatkan file di:
   - **Windows**: `C:\Users\<username>\.kaggle\kaggle.json`
   - **Mac/Linux**: `~/.kaggle/kaggle.json`
5. Set permissions (Mac/Linux): `chmod 600 ~/.kaggle/kaggle.json`

#### 3️⃣ Jalankan Analisis

**Opsi A: One-Click Launcher (Recommended)**

```bash
# Windows
run_analysis.bat

# Mac/Linux
chmod +x run_analysis.sh
./run_analysis.sh
```

**Opsi B: Manual Execution**

```bash
# Jalankan analisis data
python analisis_data_olist.py

# Jalankan dashboard
streamlit run dashboard.py
```

**Opsi C: Jupyter Notebook (Opsional)**

```bash
# Start Jupyter Notebook
jupyter notebook

# Buka Proyek_Analisis_Data_Olist.ipynb
# Jalankan semua cells
```

#### 4️⃣ Akses Dashboard

Setelah menjalankan streamlit, dashboard akan otomatis terbuka di browser:
```
http://localhost:8501
```

## 📁 Struktur Project

```
submission/
│
├── 📓 Proyek_Analisis_Data_Olist.ipynb     # Jupyter notebook (optional)
├── 📋 requirements.txt                     # Python dependencies
├── 📖 README.md                            # Documentation (you are here)
├── 📊 data/                           # All data used in analysis
|   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv            
│   ├── olist_order_items_dataset.csv                    
│   ├── olist_products_dataset.csv                 
│   ├── olist_sellers_dataset.csv                   
│   ├── delivery_performance.csv            
│   ├── olist_geolocation_dataset.csv                   
│   ├── olist_order_payments_dataset.csv                    
│   ├── olist_order_reviews_dataset.csv     
│   └── product_category_name_translation.csv                   
├── 📊 dashboard/                      # Generated data for dashboard
|   ├── dashboard.py
│   ├── orders_complete.csv                 # Complete orders dataset
│   ├── rfm_analysis.csv                    # RFM analysis results
│   ├── cluster_summary.csv                 # Customer clusters
│   ├── monthly_sales.csv                   # Monthly sales data
│   ├── delivery_performance.csv            # Delivery metrics
│   ├── state_summary.csv                   # State-level aggregation
│   ├── city_summary.csv                    # City-level aggregation
│   ├── geolocation_clean.csv               # Geographic coordinates
│   ├── customers_with_coordinates.csv      # Customers with geo data
│   ├── category_summary.csv                # Category statistics
│   ├── payment_summary.csv                 # Payment methods
│   ├── review_summary.csv                  # Review scores
│   └── product_pairs.csv                   # Cross-selling pairs
└── 🗺️ *.png                          # All image page
```

## 📊 Dataset

**Source**: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Periode Data**: September 2016 - August 2018

**Dataset Files** (9 files):
1. `olist_customers_dataset.csv` - Customer information
2. `olist_orders_dataset.csv` - Order details
3. `olist_order_items_dataset.csv` - Order items details
4. `olist_products_dataset.csv` - Product information
5. `olist_sellers_dataset.csv` - Seller information
6. `olist_geolocation_dataset.csv` - Geographic coordinates
7. `olist_order_payments_dataset.csv` - Payment information
8. `olist_order_reviews_dataset.csv` - Customer reviews
9. `product_category_name_translation.csv` - Category translations

**Size**: ~50MB (compressed)

## 🎯 Pertanyaan Bisnis yang Dijawab

### 1. **Distribusi Penjualan dan Tren**
❓ *Bagaimana distribusi penjualan berdasarkan kategori produk dan bagaimana tren penjualan dari waktu ke waktu?*

**Findings**:
- Kategori **bed_bath_table**, **health_beauty**, dan **sports_leisure** mendominasi penjualan
- Tren peningkatan signifikan dari September 2016 hingga Agustus 2018
- Puncak penjualan pada **November 2017** (Black Friday season)
- Revenue tertinggi tidak selalu dari kategori dengan volume terbanyak

### 2. **Segmentasi Pelanggan (RFM)**
❓ *Siapa pelanggan terbaik berdasarkan analisis RFM dan bagaimana karakteristik mereka?*

**Findings**:
- **Champions** (~8%): Recency rendah, frequency tinggi, monetary tinggi
- **Loyal Customers** (~25%): High frequency, good spending
- **Potential Loyalists** (~33.5%): Candidates for upselling
- **At Risk** (~28.3%): Memerlukan re-engagement strategy
- **Lost** (~5%): Perlu win-back campaigns

### 3. **Distribusi Geografis**
❓ *Bagaimana distribusi geografis pelanggan dan penjual?*

**Findings**:
- **São Paulo (SP)** mendominasi dengan **42%** total orders
- **Rio de Janeiro (RJ)** di posisi kedua dengan **13%**
- Konsentrasi tinggi di wilayah **Tenggara dan Selatan**
- Potensi ekspansi di wilayah **Utara dan Nordeste**

### 4. **Performa Pengiriman**
❓ *Bagaimana performa delivery dan on-time delivery rate?*

**Findings**:
- On-time delivery rate: **~93%**
- Rata-rata waktu pengiriman: **12 hari**
- Mayoritas pengiriman **lebih cepat** dari estimasi
- Performa grade: **Good to Excellent**

### 5. **Cross-Selling Opportunities**
❓ *Produk apa yang sering dibeli bersamaan?*

**Findings**:
- Identifikasi **top 15 product pairs**
- Peluang bundling untuk related products
- Rekomendasi untuk strategic product placement

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing

### Visualization
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive charts and graphs

### Geospatial
- **Folium** - Interactive maps
- **Streamlit-Folium** - Folium integration for Streamlit

### Dashboard
- **Streamlit** - Web application framework

### Data Source
- **Kagglehub** - Dataset download

## 📈 Key Insights & Recommendations

### 🎯 Sales Strategy
1. **Focus Marketing**: Prioritas pada top-performing categories
2. **Seasonal Campaigns**: Maximize Black Friday dan holiday seasons
3. **Category Expansion**: Ekspansi ke kategori dengan margin tinggi

### 👥 Customer Strategy
1. **Loyalty Program**: Rewards untuk Champions dan Loyal Customers
2. **Re-engagement**: Email campaigns untuk At Risk customers
3. **Win-back**: Special offers untuk Lost customers
4. **Personalization**: Targeted marketing berdasarkan RFM segments

### 🗺️ Geographic Strategy
1. **Market Penetration**: Strengthen presence di SP dan RJ
2. **Market Development**: Ekspansi ke Utara dan Nordeste
3. **Logistics Optimization**: Improve delivery di remote areas

### 🚚 Operations Strategy
1. **Maintain Quality**: Keep on-time rate above 90%
2. **Reduce Delays**: Focus on late delivery problem areas
3. **Customer Communication**: Better delivery time estimates

### 🔗 Cross-Selling Strategy
1. **Product Bundling**: Create bundles dari popular combinations
2. **Recommendations**: "Frequently bought together" features
3. **Marketing**: Targeted campaigns untuk product pairs

## 📊 Output Generated

### 📁 Data Files (13 files)
Semua data diekspor ke folder `dashboard_data/` dalam format CSV

### 🖼️ Visualizations (12+ files)
Semua grafik disimpan sebagai PNG dengan resolusi tinggi (300 DPI)

### 🗺️ Interactive Maps
- `customer_heatmap.html` - Geographic distribution heatmap

## 🐛 Troubleshooting

### Common Issues

**1. Kaggle API Error**
```bash
# Solution: Setup kaggle.json properly
# Windows: C:\Users\<username>\.kaggle\kaggle.json
# Mac/Linux: ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json  # Mac/Linux only
```

**2. Module Not Found Error**
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

**3. Dashboard Data Not Found**
```bash
# Solution: Run analysis first
run Proyek_Analisis_Data.ipynb
```

**4. Port Already in Use (Streamlit)**
```bash
# Solution: Use different port
streamlit run dashboard.py --server.port 8502
```

**5. Memory Error**
```bash
# Solution: Increase available RAM or reduce data sample size
# Edit script to sample data if needed
```

## 🤝 Contributing

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide
- Add comments untuk code yang kompleks
- Update README jika menambah features
- Test code sebelum submit PR

## 📄 License

Project ini menggunakan dataset public dari Olist yang tersedia di Kaggle untuk tujuan edukatif dan analisis.

## 👤 Author

**[Nama Anda]**
- Email: [Email Anda]
- ID Dicoding: [Username Anda]
- LinkedIn: [LinkedIn Profile]
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- **Olist** - Untuk menyediakan dataset berkualitas tinggi
- **Kaggle** - Platform untuk data science dan machine learning
- **Dicoding** - Program pembelajaran dan bootcamp
- **Streamlit** - Framework dashboard yang amazing
- **Python Community** - Untuk semua libraries yang luar biasa

## 📞 Support

Jika mengalami masalah atau memiliki pertanyaan:

1. **Check Documentation**: Baca README ini dengan teliti
2. **Check Issues**: Lihat existing issues di GitHub
3. **Create Issue**: Buat issue baru dengan detail error
4. **Contact**: Email ke [your-email@example.com]

## 🔮 Future Enhancements

Rencana pengembangan ke depan:

- [ ] Machine Learning predictions (demand forecasting)
- [ ] Real-time dashboard dengan auto-refresh
- [ ] Advanced filtering dan drill-down capabilities
- [ ] Export reports ke PDF
- [ ] Multi-language support (EN/PT-BR)
- [ ] API integration untuk real-time data
- [ ] Mobile-responsive dashboard
- [ ] Advanced clustering algorithms comparison
- [ ] Sentiment analysis dari reviews
- [ ] Forecasting & predictive analytics

## 📚 Additional Resources

### Documentation
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)
- [Folium Documentation](https://python-visualization.github.io/folium/)

### Tutorials
- [RFM Analysis Guide](https://www.kaggle.com/code/example/rfm-analysis)
- [Geospatial Analysis Tutorial](https://geopandas.org/en/stable/)
- [Streamlit Dashboard Tutorial](https://docs.streamlit.io/get-started/tutorials)

### Related Projects
- [E-Commerce Analytics Dashboard](https://github.com/example/ecommerce-dashboard)
- [Customer Segmentation Analysis](https://github.com/example/customer-segmentation)

## ⭐ Star History

Jika project ini membantu, berikan ⭐ star di GitHub!

---

<div align="center">

**Made with ❤️ for Data Analysis Learning**

**Happy Analyzing! 📊✨**

[⬆ Back to Top](#-brazilian-e-commerce-olist-data-analysis-project)

</div>