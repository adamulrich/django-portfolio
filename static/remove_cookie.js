
const cities = 'cities=';

function removeCookie(id) {
    currentCookie = cookieValue;
    console.log(id)

    // create list
        temp_list = currentCookie.split(',');

        for( var i = 0; i < temp_list.length; i++){ 
    
            if ( temp_list[i].toString() === id.toString()) { 
                console.log('here');
                temp_list.splice(i, 1); 
            }
        
        // save new cookie as csv
        newCookie = temp_list.toString();
        console.log(newCookie);
        document.cookie = cities + newCookie;
        location.reload();
    }

}

const cookieValue = document.cookie
  .split("; ")
  .find((row) => row.startsWith(cities))
  ?.split("=")[1];


