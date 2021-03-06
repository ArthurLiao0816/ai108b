# Application of Fourier transform in speech recognition
***

## 大綱
* [甚麼是傅立葉轉換呢?](#甚麼是傅立葉轉換呢?)
* [語音辨識的原理](#語音辨識的原理)
* [語音辨識的應用](#語音辨識的應用)
* [實作](#實作)

## 甚麼是傅立葉變換呢?

### 變換?
* 在講甚麼是傅立葉變換之前，要先認識「變換」的概念。甚麼是變換呢?高中在學向量的時候，老師常常先將向量畫在xy軸上，然後再以數學表示法將其寫在旁邊。這種從圖可以變成數學式、數學式也可以變成圖的關係，就是一種變換。

### 傅立葉變換
* 既然傅立葉變換中帶有「變換」這兩個字，根據我剛剛所述，就代表這之中一定有至少兩個不同的東西可以彼此互相變來變去，而這兩個東西，分別是信號的時域和頻域。在這兩種不同的「域」種鎖的到的數據，可以幫助人們分析自然界的各種信號。

## 語音辨識的原理
* 人類講話的聲音可以以『示波器』測量成一個隨時間變化的波形信號，這種信號對時間的關係，稱之為「時域」，在電腦對信號進行分析時，通常信號會先被轉換成在不同頻率下對應的振幅及相位，稱之為「頻域」，轉換的公式稱為「傅立葉變換」，信號經過每隔一段時間取樣，就得到可以進行分析的數位音檔，附檔名通常是 wav。
* 為了方便作語音辨識，與影像一樣，我們會對語音作特徵抽取(Feature Extraction)，目前有 FBank、MFCC(Mel frequency cepstral coefficients) 兩種，特徵抽取前須先對聲音作前置處理：
1. 幀(Frame)切割：通常每幀是25ms，幀與幀之間重疊10ms，以避免邊界信號的遺漏。

2. 信號加強：針對高頻信號作加強，使信號更清楚。

3. 加窗(Window)：目的是消除各個幀兩端可能會造成的信號不連續性，常用的窗函數有方窗、漢明窗等。

4. 去除雜訊(denoising or noise reduction)。

## 語音辨識的應用
### 新一代 Google 助理
![](https://img.technews.tw/wp-content/uploads/2019/01/08152618/google-624x367.jpg)
* 隨著循環神經網路（RNN，Recurrent Neural Networks）的發展，Google 開發出全新語音辨識以及語言理解模型，讓原本需要 100 GB 空間的模型縮減成不到 1 GB 的一半。有了這些新的模型，Google 助理應用的 AI 技術就能在使用者的裝置上執行。這個突破讓 Google 可以打造讓使用者能在裝置上進行零時差語音操控的新一代 Google 助理， 甚至在沒有網路的狀態下也能執行。

### 兒童語音辨識技術
![](https://img.technews.tw/wp-content/uploads/2019/02/01153503/shutterstock_741570274-624x351.jpg)
* 隨著裝載語音助理裝置如智慧音箱等愈趨普及，家長們也發現家中幼童很自然地會想要與語音助理互動、下口語指令，以完成他們的需求，譬如播放兒童歌曲或詢問其他資訊。但由於語音助理背後的資料庫為成人語料，幼童口語其實與成人口語有甚多差異，導致語音助理在理解孩童語言時產生困難，也無法提供孩童期待的回應，致使兒童的使用體驗不佳。兒童語音辨識相關應用廣泛，對 3 歲以上幼童而言，他們迫切需要利用語言來表達自我，同時從回饋中獲取知識，而父母通常會更願意投資幼教玩具器材。近來各廠商也注意到此塊需求，不管是美國科技大廠如 Amazon 推出兒童專用的智慧音箱 Echo Dot Kids Edition；中文市場也有如百度與聲智科技合作，在其帶螢幕音箱小度在家 1S 推出兒童智慧成長模式；台灣則有遠傳推出小愛講、小狐狸，其他玩具廠商也陸續推出可跟孩童對話的玩具。以上均可看出，語音技術應用在兒童教育或娛樂市場中正不斷成長。不過，相關廠商在切入兒童利基市場時，確實遭遇到更多技術層面上的挑戰，包括兒童使用者的童音音頻較高，兒童語言的語音和語意均擁有更多不確定性和複雜性，溝通互動時常常出奇不意，邏輯與成人不同，導致以成人語言做為語料庫的 Amazon Echo 和 Google Assistant 在理解兒童語言時，發生錯誤的機率提高。有心耕耘兒童市場的廠商，勢必得從建造兒童語料庫開始，發展出兒童語音辨識模型並經過驗證，或直接尋找具備此方面技術的合作夥伴。

### 亞馬遜正在開發可辨識情緒的產品
![](https://img.technews.tw/wp-content/uploads/2018/01/17202528/20180117202508-624x403.jpg)
* 亞馬遜在 2017 年申請的一份專利顯示，語音辨識軟體透過用戶聲音來分析和確認用戶的感受，可辨識快樂、憤怒、悲傷、難過、恐懼、厭惡等多種情緒狀態。在應用中這項技術可監控用戶的情緒狀態，比如用戶處於生病中疲憊的狀態，準確辨識後語音助手會向用戶提供相應的幫助，可準確區分用戶的聲音和環境背景雜音。

## 實作
1. pip install SpeechRecognition
   pip install pipwin
   pipwin install pyaudio

2. [Code](practice.py)

3. py .\practice.py

4. 說一段話

5. [結果(Click Me ^^)](result.png)