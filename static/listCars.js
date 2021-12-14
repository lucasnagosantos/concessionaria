$( document ).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:5000/readAllCars",
        type: 'GET',
        success: function(res) {
            renderCars(res)
            
        }
    });
});

function renderCars(carList){
    carList = eval(carList)

    carList.forEach(car => {
        $("#car-list").append(`
            &nbsp;&nbsp;&nbsp;&nbsp;
            <div class="col-sm-12 col-md-6 col-lg-3 card mt-3">
                <div class="card-body" style="text-align: center;">
                ${car['name']} - ${car['brand']}
                </div>
                <img src="${car['imgPath']}">

                <div class="card-footer" style="text-align: center;">
                <b>Valor</b>: ${car['value']}<br>
                <b>Ano</b>: ${car['carYear']}<br>
                <b>Condição</b>: ${car['carType']}
                </div>
            </div>
    
        `)
    });


    
}