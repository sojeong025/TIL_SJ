/* 
  아래에 코드를 작성해주세요.
*/

const searchBtn = document.querySelector('.search-box__button')
const my_API = `2c57106b61b84f1ef3160b3893a4dd75`

searchBtn.addEventListener('click', fetchAlbums)

function fetchAlbums(page=1, limit=10){
  let keyword = document.querySelector('.search-box__input').value
  
  axios({
    method : 'get',
    url : 'http://ws.audioscrobbler.com/2.0',
    params : {
      method : 'album.search',
      album : keyword,
      api_key : my_API,
      page: page,
      limit: limit,
      format : 'json'
    }
  })
  
  .then((response) => {
    let albums = response.data.results.albummatches.album
    console.log(albums)
    
    albums.forEach(album => {
      // 이미지 태그 만들기
      const cardImg = document.createElement('img')
      cardImg.src = album.image[1]['#text']
      
      // div 태그 만들고 클래스 부여햐기
      const card = document.createElement('div')
      card.classList.add('search-result__card')
      
      const cardBody = document.createElement('div')
      card.classList.add('search-result__text')
      
      cardBody.innerHTML = `
      <h2>${album.artist}</h2>
      <p>${album.name}</p>
      `
      card.append(cardImg, cardBody)

      document.querySelector('.search-result').appendChild(card)
      
    })


  })
  .catch((error) =>{
    alert('잠시 후 다시 시도해주세요')
  })
  
}
