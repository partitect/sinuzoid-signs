Sine Dalga Oluşturucu

Bu Flask web uygulaması, belirli bir frekans ve genlik ile veya belirli
bir değer aralığında sinüs dalgaları oluşturmanıza olanak tanır.

Kurulum Gerekli bağımlılıkları yükleyin: pip install flask matplotlib
numpy Projeniz için yeni bir dizin oluşturun ve içine gidin: mkdir
sine-wave-generator cd sine-wave-generator app.py adlı yeni bir dosya
oluşturun ve orijinal istemde sağlanan kodu içine yapıştırın.

static adlı yeni bir dizin oluşturun ve index.html, frekans.html,
arrange.html, resultfreqency.html ve resultarrange.html dosyalarını
içine kopyalayın.

Kullanım Flask geliştirme sunucusunu başlatmak için aşağıdaki komutu
çalıştırın:

flask run Ardından web tarayıcınızı açın ve http://localhost:5000/
adresine gidin.

Belirli bir frekans ve genlik ile bir sinüs dalgası oluşturmak için,
"Frekans" sekmesine tıklayın ve ilgili alanlara istediğiniz değerleri
girin. Ardından "Generate" düğmesine tıklayın.

Belirli bir değer aralığında bir sinüs dalgası oluşturmak için,
"Arrange" sekmesine tıklayın ve aralıktaki başlangıç ve bitiş
değerlerini ilgili alanlara girin. Ardından "Generate" düğmesine
tıklayın.

Oluşturulan sinüs dalgası, ilgili sayfada bir grafik olarak
görüntülenecektir. Ayrıca, "Save" düğmesine tıklayarak grafiği
bilgisayarınıza kaydedebilirsiniz.

Örnekler Sine dalga oluşturucuyu nasıl kullanacağınıza dair bazı
örnekler:

1 Hz frekans ve 2 genlik ile bir sinüs dalgası oluşturmak için,
"Frekans" sekmesine tıklayın ve "Frekans" alanına 1 ve "Genişlik"
alanına 2 girin. Ardından "Generate" düğmesine tıklayın. 0 ile 10
arasındaki değer aralığında bir sinüs dalgası oluşturmak için, "Arrange"
sekmesine tıklayın ve "x1" alanına 0 ve "x2" alanına 10 girin. Ardından
"Generate" düğmesine tıklayın. Farklı sinüs dalgaları oluşturmak için
farklı değerlerle denemeler yapabilirsiniz.
