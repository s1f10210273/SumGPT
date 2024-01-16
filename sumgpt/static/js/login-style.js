$(window).on('load',function(){
//ローディングエリア（splashエリア）を1.5秒でフェードアウトする記述
      $('body').addClass('appear');//フェードアウト後bodyにappearクラス付与
      var h = $(window).height();//ブラウザの高さを取得
      $(".splashbg").css({
        "border-width":h,//ボーダーの太さにブラウザの高さを代入
        "animation-name":"backBoxAnime"//animation-nameを定義
      }); 
});