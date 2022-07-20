from ast import If
from flask import Flask, redirect
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/welcome", methods=['GET', 'POST'])  # ini link pada url web flask
def welcome():  # ini function untuk setiap link pada flask
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = request.form['username']
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('hello_world'))

@app.route("/diagnosa", methods=['GET', 'POST'])  # ini link pada url web flask
def diagnosa():  # ini function untuk setiap link pada flask
    if request.method == 'POST':
        name = session['username']
        result = request.form['result']
        if result == "y" or "Y":
            return render_template('diagnosa.html', name=name)
        else:
            return render_template('index.html')
    else:
        return redirect(url_for('hello_world'))


@app.route("/result", methods=['GET', 'POST'])  # ini link pada url web flask
def akhir():  # ini function untuk setiap link pada flask
    if request.method == 'POST':
        name = session['username']
        result = request.form['result']

        # start logic system pakar
        if result == "f,h":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,c,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,d,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,e,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c,d,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c,e,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "c,d,e,f":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Diabetes Melitus Tipe 2."
            var_2 = "1) Sel-sel tubuh menjadi tidak sensitif dan tidak bisa menggunakan insulin dengan baik juga belum diketahui secara pasti."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat dan mengonsumsi makanan yang bergizi."
            var_6 = "3) Pemberian Obat. Metformin, Glinide, Thiazolidinesdiones (dengan resep dokter)."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,c":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "c,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "c,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "d,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Awal Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,c":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "c,d,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi Gejala Diabetes."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,c,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi GDiabetes Meltus Tipe 1."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,c,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi GDiabetes Meltus Tipe 1."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "b,c,e,d":
            var_1 = "Diagnosa Awal, Anda Terdeteksi GDiabetes Meltus Tipe 1."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        elif result == "a,b,c,d,e":
            var_1 = "Diagnosa Awal, Anda Terdeteksi GDiabetes Meltus Tipe 1."
            var_2 = "1) Faktor genetika atau keterunan."
            var_3 = "2) Gaya hidup kurang aktif, obesitas, dan pertambahan usia."
            var_4 = "1) Diet Dan Berolahraga."
            var_5 = "2) Menerapkan hidup sehat."
            var_6 = "3) Mengonsumsi makanan yang bergizi."
            var_7 = "4) Operasi Bariatrik yang bertujuan untuk mengubah bentuk saluran pencernaan agar porsi makanan dapat dibatasi dan nutrisi yang terserap berkurang."
            var_8 = "5) Pemeriksaan Kesehatan Rutin."
            var_9 = "Untuk Hasil Yang Lebih Akurat Silakan Untuk Cek Gula Darah Anda Ke Tempat Kesehatan Terdekat."
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
        else:
            var_1 = "Kombinasi Kriteria yang anda masukan belum terdaftar pada perpustkaan sistem"
            var_2 = " "
            var_3 = "Kombinasi Kriteria yang anda masukan belum terdaftar pada perpustkaan sistem"
            var_4 = " "
            var_5 = " "
            var_6 = "Kombinasi Kriteria yang anda masukan belum terdaftar pada perpustkaan sistem"
            var_7 = " "
            var_8 = " "
            var_9 = "Kombinasi Kriteria yang anda masukan\nbelum terdaftar pada perpustkaan sistem"
            return render_template('result.html', var1=var_1, var2=var_2, var3=var_3, var4=var_4, var5=var_5, var6=var_6, var7=var_7, var8=var_8, var9=var_9, name=name)
    else:
        return redirect(url_for('hello_world'))

@app.route("/indexweb", methods=['GET', 'POST'])
def indexweb():
    return render_template('indexweb.html')

@app.route("/result/<params>") # ini link pada url web flask
def result(params): # ini function untuk setiap link pada flask
    return str(params)