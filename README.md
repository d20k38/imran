# İmran Neocities Otomatik Dosya Merkezi

Bu paket, `imrann.neocities.org` sitesindeki dosyaları otomatik olarak listeleyen bir ana sayfa sağlar.

## Ne yapar?

- PDF, JPG, PNG, WEBP, HTML, MP4, DOCX, XLSX vb. dosyaları listeler.
- Klasörleri gösterir.
- Dosya adına göre arama yapar.
- Dosya türüne göre filtreler.
- PDF/görsel/HTML/video dosyalarını doğrudan Neocities adresinden açar.
- Neocities API anahtarı `index.html` içine konulmaz.
- GitHub Actions, Neocities API'den listeyi alır ve `files.json` dosyasını Neocities'e yükler.
- 15 dakikada bir otomatik kontrol yapılır. Ayrıca GitHub Actions içinden elle çalıştırılabilir.

## Kurulum

### 1. GitHub'da yeni bir repository oluşturun

Örneğin:

`neocities-dosya-merkezi`

ZIP içindeki dosyaları bu repository'ye yükleyin.

Klasör yapısı:

```
index.html
files.json
scripts/build_files_json.py
.github/workflows/update-neocities-files.yml
```

### 2. Neocities API anahtarını oluşturun

Neocities hesabınıza giriş yaptıktan sonra API anahtarınızı Neocities'in API bölümünden oluşturun.

**API anahtarını bana göndermeyin ve `index.html` içine yazmayın.**

### 3. GitHub Secret ekleyin

GitHub repository:

`Settings → Secrets and variables → Actions → New repository secret`

Adı:

`NEOCITIES_API_KEY`

Değeri:

Neocities API anahtarınız.

### 4. İlk çalıştırma

GitHub:

`Actions → Neocities Dosya Listesini Güncelle → Run workflow`

seçeneğine basın.

Başarılı çalışınca Neocities ana dizininizde:

`files.json`

oluşur.

### 5. index.html'yi Neocities'e yükleyin

ZIP'teki `index.html` dosyasını Neocities ana dizinine yükleyin.

**Önemli:** Mevcut `index.html` dosyanız varsa, önce yedeğini alın.

## Otomatik çalışma

Workflow:

`*/15 * * * *`

ile yaklaşık 15 dakikada bir çalışır.

GitHub Actions zamanlamaları yoğunluk nedeniyle birkaç dakika gecikebilir.

Neocities'in API dokümanı da API kullanımında gereksiz yoğun isteklerden kaçınılmasını ve tekrarlayan site güncellemelerinin makul aralıklarla yapılmasını öneriyor.

## Sonuç

Yeni bir PDF/JPG/HTML/MP4 dosyasını Neocities'e yüklediğinizde:

Neocities → GitHub Actions → files.json → Dosya Merkezi

zinciriyle liste güncellenir.

API anahtarı tarayıcıya gönderilmez.

## Güvenlik

- API anahtarını sadece GitHub Secret olarak tutun.
- ZIP'e API anahtarı yazmayın.
- `index.html` içine API anahtarı koymayın.
- GitHub repository'sini herkese açık yapacaksanız Secret'ın yalnızca GitHub Secrets içinde olduğundan emin olun.
