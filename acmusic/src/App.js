import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [time, setTime] = useState(new Date());
  const [videos, setVideos] = useState([]);
  const [weather, setWeather] = useState(null);
  const [city, setCity] = useState(null);
  const [version, setVersion] = useState('Wild World/City Folk');
  const appid = '20d69df1e454303a5e3a07e410dabcc1';
  
  useEffect(() => {
    let file;

    switch(version) {
      case 'GameCube':
        file = 'videos_gc.txt';
        break;
      case 'Wild World/City Folk':
        file = 'videos_ww.txt';
        break;
      case 'New Leaf':
        file = 'videos_nl.txt';
        break;
      case 'New Horizons':
        file = 'videos_nh.txt';
        break;
      default:
        file = 'videos_ww.txt';
    }
    fetch(`/${file}`)
      .then(response => response.text())
      .then(text => {
        const urls = text.split('\n').filter(line => line.trim() !== '');
        setVideos(urls);
      })
      .catch(error => console.error('Video error:', error));
  }, [version]);

  useEffect(() => {
    if(navigator.geolocation){
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;

          fetch(`https://api.openweathermap.org/geo/1.0/reverse?lat=${lat}&lon=${lon}&limit=1&appid=${appid}`)
          .then(response => response.json())
          .then(data => {
            if (data && data[0]) {
              setCity(data[0].name);
            }
          })
          .catch(error => console.error('City error:', error));
        }
      )
    }
  }, []);

  useEffect(() =>{
    if(!city) {
      return;
    }

  const fetchWeather = () => {
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${appid}&units=metric`)
      .then(response => response.json())
      .then(data => {
        if (data.weather && data.weather[0]) {
          setWeather(data.weather[0].main);
        }
      })
      .catch(error => console.error('Weather error:', error));
  };

    fetchWeather();
    const weatherInterval = setInterval(fetchWeather, 60000);
    return () => clearInterval(weatherInterval);
  }, [city]);

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const formatTime = (date) => {
    return date.toLocaleTimeString('es-ES', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    });
  };

  const getDark = () => {
      const hour = time.getHours();

      if(hour >= 20 || hour < 4){
        return 0.8;
      }
      else if(hour === 4 || hour === 19){
        return 0.6;
      }
      else if(hour === 5){
        return 0.4;
      }
      else if(hour === 6 || hour === 18){
        return 0.2;
      }
      else if(hour === 7 || hour === 17){
        return 0.1;
      }
      else if(hour >= 8 || hour < 17){
        return 0;
      }
  }

  const currentVideo = time.getHours();
  const opacity = getDark();
  const isRaining = weather === 'Rain' || weather === 'Drizzle';
  const isSnowing = weather === 'Snow';
  const isCloudy = weather === 'Clouds';
  return (
    <div className="App"
    style={{
      fontFamily: 'Animal Crossing',
    }}>
      <header className="App-header"
      style={{
          backgroundImage:
            `linear-gradient(rgba(${(isRaining || isCloudy || isSnowing) ? 73 : 12}, ${(isRaining || isCloudy || isSnowing) ? 73 : 12}, 65, ${(isRaining || isCloudy || isSnowing) ? 0.8 : opacity}), rgba(0, 0, 0, ${opacity})), 
            url('/background.png')`
      }}>
        <div className="Clock"
          style={{ 
          position: 'absolute', 
          top: '20px', 
          right: '20px', 
          fontSize: '2rem',
          backgroundColor: 'rgba(255, 250, 232)',
          padding: '15px 30px',
          borderRadius: '63% 37% 54% 46% / 55% 48% 52% 45%',
          boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.7)',
          color: 'rgba(113, 101, 77)',
          animation: 'morph 10s linear infinite, float 5s ease-in-out infinite'
        }}>
          <p style={{
            fontWeight: 'bold',}}>
            {formatTime(time)}</p>
          <p style={{
            fontSize: '1.5rem',
          }}>
            📍{city || 'Locating city...'}
            {isRaining && ' 🌧️'}
            {isSnowing && ' 🌨️'}
            {isCloudy && ' ☁️'}
            {!isRaining && !isSnowing && !isCloudy && city && ' ☀️'}
          </p>
        </div>

        <iframe style={{
            borderRadius: '30px',
            boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.7)'
          }}
          key={currentVideo}
          width="560" 
          height="315"
          src={videos[currentVideo + (isRaining && !(version === 'GameCube') && 24) + (isSnowing && !(version === 'GameCube') && 48)] + "&autoplay=1&loop=1"}
          title="YouTube video player"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; loop"
          referrerPolicy="strict-origin-when-cross-origin"
          allowFullScreen>
        </iframe>
        <p></p>
        Version
        <div style={{ display: 'flex', gap: '10px'}}>
        <button style={version === 'GameCube' ? {backgroundColor: 'rgba(255, 218, 23)'} : {} } onClick={() => setVersion('GameCube')} className='Version-button'>GameCube</button>
        <button style={version === 'Wild World/City Folk' ? {backgroundColor: 'rgba(255, 218, 23)'} : {} } onClick={() => setVersion('Wild World/City Folk')} className='Version-button'>Wild World/City Folk</button>
        <button style={version === 'New Leaf' ? {backgroundColor: 'rgba(255, 218, 23)'} : {} } onClick={() => setVersion('New Leaf')} className='Version-button'>New Leaf</button>
        <button style={version === 'New Horizons' ? {backgroundColor: 'rgba(255, 218, 23)'} : {} } onClick={() => setVersion('New Horizons')} className='Version-button'>New Horizons</button></div>
      </header>
    </div>
  );
}

export default App;