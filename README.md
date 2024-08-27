Location Tracker
Location Tracker uygulaması, kullanıcıların konum kayıtlarını izlemek ve yönetmek için oluşturulmuş bir Django uygulamasıdır. Bu proje, kullanıcı bilgilerini ve konum kayıtlarını veritabanında saklar ve basit bir web arayüzü sağlar.

Özellikler
Kullanıcı bilgilerini (isim ve soyisim) ekleyin ve yönetin.
Konum kayıtlarını (tarih, saat, enlem, boylam) ekleyin ve görüntüleyin.
Veritabanında indeksleme ve performans optimizasyonu.
Başlangıç
Bu kılavuz, projeyi yerel ortamınızda çalıştırmak için gerekli adımları içerir.

Ön Gereksinimler
Python 3.x
Django 4.x
(Opsiyonel) Bir veritabanı (SQLite varsayılan olarak kullanılır)
Kurulum
Python ve Pip Kurulumu

Python ve pip'in sisteminizde kurulu olduğundan emin olun. Python 3.x ve pip yüklemek için:

brew install python
Proje Klasörüne Geçiş

Proje klasörüne gidin:

cd /path/to/location_tracker
Sanal Ortam Oluşturma ve Aktifleştirme

Sanal ortam oluşturun ve aktif hale getirin:

python3 -m venv myenv
source myenv/bin/activate
Gerekli Paketleri Yükleyin

requirements.txt dosyasındaki bağımlılıkları yükleyin:

pip install -r requirements.txt
Veritabanı Migration'larını Oluşturma ve Uygulama

Migration dosyalarını oluşturun ve veritabanını güncelleyin:

python manage.py makemigrations
python manage.py migrate
Veritabanını Rastgele Verilerle Doldurma

Veritabanını örnek verilerle doldurmak için:

python manage.py populate_db
Geliştirme Sunucusunu Başlatma

Django geliştirme sunucusunu başlatın:


python manage.py runserver
Tarayıcınızda http://127.0.0.1:8000/ adresine giderek uygulamanızı görüntüleyebilirsiniz.

Kullanım
Ana sayfada kullanıcı bilgilerini ve konum kayıtlarını görüntüleyebilirsiniz.
Veritabanına veri eklemek için uygun formları kullanın.
