#概要
細音啓先生の作品「黄昏色の詠使い」などに登場する独自言語(いわゆる「セラフェノ」)の使用を支援します．  
Twitterの[@miqveqs_clue][]で稼働しますが，筆者がスクリプトを走らせている間にのみ機能します．

#機能
* [@miqveqs_clue][]にセラフェノの単語をreplyで送ると，その単語の日本語訳をreplyで返します．
* [@miqveqs_clue][]に日本語の単語をreplyで送ると，その単語のセラフェノ訳をreplyで返します．
* [@miqveqs_clue][]に「類義語 (セラフェノの単語)」という形式でreplyを送ると，その単語の日本語訳およびその訳の類義語をreplyで返します．
* [@miqveqs_clue][]に「類義語 (日本語の単語)」という形式でreplyを送ると，その単語のセラフェノ訳が登録されている場合はそのセラフェノ訳をreplyで返し，セラフェノ訳が登録されていない場合はその日本語の単語の類義語に対するセラフェノ訳をreplyで返します．

[@miqveqs_clue]: https://twitter.com/miqveqs_clue　“@miqveqs_clue”

#使用データ
類義語検索のデータベースとして，WordNetを使用しています．  
GitHubのソースにはWordNetのデータは含めていません．

日本語ワードネット （1.1版）© 情報通信研究機構, 2009-2010　 
linked to http://nlpwww.nict.go.jp/wn-ja/