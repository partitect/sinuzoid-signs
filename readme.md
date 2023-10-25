# Sinüsoidal Sinyali Üretme Uygulaması

Bu proje, kullanıcı girdilerine dayalı sinüsoidal sinyalleri oluşturmayı ve göstermeyi amaçlayan bir Flask web uygulamasını içerir. Bu projeyi başlatmak için aşağıdaki adımları izleyin:

## Proje Kurulumu

1. **Proje Dizinini Oluşturun:**

   - Python'un sistemde yüklü olduğundan emin olun. Yüklü değilse resmi Python web sitesinden indirip kurun.

   - Bir proje dizini oluşturun ve komut satırı terminalinizde bu dizine gidin.

   - Proje dizini içinde, proje bağımlılıklarını izole etmek için bir sanal ortam (virtual environment) oluşturun:

     ```
     python -m venv venv
     ```

   - Sanal ortamı etkinleştirin:

     - Windows için:

       ```
       venv\Scripts\activate
       ```

     - macOS ve Linux için:

       ```
       source venv/bin/activate
       ```

2. **Gerekli Kütüphaneleri Yükleyin:**

   - Sanal ortam etkinleştirildiğinde, "requirements.txt" dosyasındaki gereken kütüphaneleri aşağıdaki komutla yükleyin:

     ```
     pip install -r requirements.txt
     ```

## Proje Yapısı

- Projelerinizi ve klasörlerinizi aşağıdaki gibi düzenleyin:

     ```
     your_project/
     ├── app.py
     ├── static/
     │   ├── sinuzoid-frequency.png
     │   └── sinuzoid-arrange.png
     ├── templates/
     │   ├── index.html
     │   ├── frekans.html
     │   ├── arrange.html
     │   ├── resultfreqency.html
     │   └── resultarrange.html
     └── requirements.txt
     ```

- Web sayfalarınızı oluşturmak için HTML şablonlarına ihtiyacınız olacak. Flask yönlendirmeleriniz (`index`, `frekans`, `arrange`, `resultfreqency`, `resultarrange`) bu şablonları kullanarak web sayfalarını görüntüleyecek.

## Uygulamayı Başlatma

- Proje dizininde, Flask uygulamasını aşağıdaki komutla başlatın:

```
flask run
```

- Bu, Flask geliştirme sunucusunu başlatacak ve sunucunun çalıştığı URL'yi gösteren bir çıktı sağlayacaktır. Genellikle uygulamanızın erişilebilir olduğu bir URL sunacaktır, genellikle `http://127.0.0.1:5000/` gibi. Tarayıcınızda bu URL'yi açarak Flask web uygulamanıza erişebilirsiniz.

## Uygulamayı Kullanma

- Farklı yönlere (`/`, `/frekans`, `/arrange`) giderek web uygulamanızla etkileşimde bulunabilir ve sonuçları görebilirsiniz.

## Uygulamayı Durdurma

- Flask geliştirme sunucusunu durdurmak için terminalinizde `Ctrl+C` tuşlarına basabilirsiniz.

Bu adımlar, Flask web uygulamanızla başlamanıza yardımcı olmalıdır. Projeyi özelleştirebilir ve gerektiğinde daha fazla özellik ekleyebilirsiniz. Herhangi bir sorunla karşılaşırsanız veya projenizle ilgili belirli sorularınız varsa, sormaktan çekinmeyin.

Telat Kaya