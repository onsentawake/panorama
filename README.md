# panorama
#勉強会でいただいたファイル

 #今後の課題点：音の切り替わり時にクリックノイズが発生しているため、それを解消したい。クロスフェードでなんとかなる？が記述がわからない
 
 
 このあたりが参考になりそう
 http://ja.voidcc.com/question/p-pmxfnmfy-mh.html
 https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
 
 
 
 def play_wave(stream, chunks): #引数2つ
    chunk = np.concatenate([chunks]) * 0.25#音量？
    fade = 200  #ms単位
    fade_in = np.arange(0., 1., 1/fade)　#floatしか対応していないbyみどりまて　　なむぱいのarangeメソッド。
    fade_out = np.arange(1., 0., -1/fade)
    chunk[:fade] = np.multiply(chunk[:fade], fade_in)
    chunk[-fade:] = np.multiply(chunk[-fade:], fade_out)
    stream.write(chunk.astype(np.float32).tostring())

## Installation

Mac

```bash
brew install portaudio
pipenv install
python pnrmtest.py
```
