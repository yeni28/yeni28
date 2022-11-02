/* 
  아래에 코드를 작성해주세요.
*/

const keyword = document.querySelector(".search-box__input")
const searchBtn = document.querySelector(".search-box__button")
searchBtn.addEventListener('click', fetchAlbums)

function fetchAlbums (page=1, limit=10) {

  axios({
    method: 'get',
    url: `http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword.value}&api_key=f2aae170c9d25fc8dfb8c0fef8c790e9&format=json&page=${page}&limit=${limit}`
  })
  .then((response) =>{
    // console.log(response)
    const albums = response.data.results.albummatches.album
    albums.forEach((music) => {
      const musiclist = document.createElement('div')
      musiclist.classList.add('search-result__card')
      // console.log(albums)
      //이미지 태그
      const cardimg = document.createElement('img')
      cardimg.src = music.image[1]["#text"]

      // 뮤직 텍스트
      const musictext = document.createElement('div')
      musictext.classList.add('search-reuslt__text')

      const artist = document.createElement('h2')
      artist.innerText = music.artist

      const name = document.createElement('p')
      name.innerText = music.name

      musictext.appendChild(artist)
      musictext.appendChild(name)

      musiclist.append(cardimg)
      musiclist.appendChild(musictext)

      const allmusic = document.querySelector('.search-result')
      allmusic.appendChild(musiclist)
    }
  )
  })
  .catch((error)=>{
    alert('잠시 후 다시 시도해주세요')
  })
}

