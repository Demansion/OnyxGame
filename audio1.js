function soundClick() {
    var audio = new Audio(); // Создаём новый элемент Audio
    audio.src = 'music.mp3'; // Указываем путь к звуку "клика"
    audio.pause; // Автоматически запускаем
    audio.volume = 0.1;
  }