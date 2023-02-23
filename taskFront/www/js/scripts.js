//Mostrar

const url = "http://10.0.1.208:8000/tarea-post";
const urlGet = "http://10.0.1.208:8000/tarea-get";
const urlEliminar = "http://10.0.1.208:8000/tarea-eliminar";
const url1 = "http://10.0.1.208:8000/tarea-put";

//Meotodo Get
// const botonget = document.getElementById("get");

// botonget.addEventListener("click", (e) => {
//   e.preventDefault();

//   var cod = document.getElementById("producto").value;
//   var combo = document.getElementById("producto");
//   var selected = combo.options[combo.selectedIndex].text;

//   axios

//     .get(urlGet)
//     .then((resp) => {
//       const data = resp.data["datos"];
//       console.log(resp.data);

//       // Elimina el contenido anterior del elemento #texto
//       const textoEl = document.getElementById("texto");
//       textoEl.innerHTML = "";

//       // Itera sobre cada elemento en el objeto de respuesta
//       data.forEach((elemento) => {

//         const nuevoElemento = document.createElement("div");
//         nuevoElemento.classList.add("elemento");

//         // Agrega el contenido al nuevo elemento
//         console.log(elemento);
//         nuevoElemento.innerHTML = `

//         <br/>
//           <p>Id: ${elemento.idTarea}</p>
//           <p>Nombre: ${elemento.title}</p>
//           <p>Status: ${elemento.status__opsnombre}</p>
//           <p>Fecha de Creacion:</p>
//           <P>${elemento.created_at}</p>

//           <button onClick="editarPut(${elemento.idTarea})" type="button" data-toggle="modal" data-target="#Editar" class="btn btn-success">
//             Editar
//           </button>

//           <button onClick="eliminar(${elemento.idTarea})" id="eliminar" type="button" class="btn btn-danger">
//             Eliminar
//           </button>

//           <br/>

//         `;

//         // Agrega el nuevo elemento al contenedor
//         textoEl.appendChild(nuevoElemento);
//       });
//     })
//     .catch((error) => {
//       console.log(error);
//     });
// });

function cargaDatos1() {
  var cod = document.getElementById("producto").value;
  var combo = document.getElementById("producto");
  var selected = combo.options[combo.selectedIndex].text;

  axios

    .get(urlGet)
    .then((resp) => {
      const data = resp.data["datos"];
      console.log(resp.data);

      // Elimina el contenido anterior del elemento #texto
      const textoEl = document.getElementById("texto");
      textoEl.innerHTML = "";

      // Itera sobre cada elemento en el objeto de respuesta
      data.forEach((elemento) => {
        const nuevoElemento = document.createElement("div");
        nuevoElemento.classList.add("elemento");

        // Agrega el contenido al nuevo elemento
        console.log(elemento);
        nuevoElemento.innerHTML = `

        <br/>
          
          <table class="table">
            <thead>
              <tr>
                <th>Id</th>
                <th>Nombre</th>
                <th>Status</th>
                <th>Fecha</th>
                </tr>
              </tr>
            </thead>
            <tbody class='container'>

            <div> 
            <td>${elemento.idTarea}</td> 
            <td>${elemento.title}</td> 
            <td>${elemento.status__opsnombre}</td> 
            <td>${elemento.created_at}</p> 
            
      
            <button onClick="editarPut(${elemento.idTarea})" type="button" data-toggle="modal" data-target="#Editar" class="btn btn-success">
              Editar 
            </button>  
  
            <button onClick="eliminar(${elemento.idTarea})" id="eliminar" type="button" class="btn btn-danger">
              Eliminar
            </button>  
            </div>
          </tbody> 
          
  
      </table>
         
        
 
        `;

        // Agrega el nuevo elemento al contenedor
        textoEl.appendChild(nuevoElemento);
        document.getElementById("cuerpo").appendChild(nuevoElemento);
      });
    })
    .catch((error) => {
      console.log(error);
    });
}

// CARGAR DATOS NO FUNCIONA

// Funcion eliminar
function eliminar(id) {
  console.log(id);
  axios
    .delete(urlEliminar, { params: { idTarea: id } })

    .then((resp) => {
      location.reload();
    })
    .catch((error) => {
      console.error(error);
      alert("Ha ocurrido un error al eliminar el recurso");
    });
}

// METODO POST
const btnPost = document.getElementById("post");
const inputPost = document.getElementById("title");

console.log(btnPost);

btnPost.addEventListener("click", (e) => {
  e.preventDefault();

  const input = inputPost.value;
  var cod = document.getElementById("producto").value;

  var combo = document.getElementById("producto");
  var selected = combo.options[combo.selectedIndex].value;

  if (input.trim() === "") {
    alert("Por favor, introduce un texto válido");
    return;
  }

  axios
    .post(url, {
      title: input,
      status: selected,
    })
    .then((resp) => {
      // Si la solicitud se completa correctamente, muestra un mensaje de confirmación

      console.log("a");
      location.reload();
    })
    .catch((error) => {
      // Si hay algún error, muestra un mensaje de error
      console.error(error);
      alert("Ha ocurrido un error al crear la tarea");
    });
});

function editarPut(id) {
  console.log(id);
  localStorage.setItem("idTarea", id);
  const inputPut = document.getElementById("newTitle");
  const input = inputPut.value;
  console.log(input);

  var cod = document.getElementById("producto").value;

  var combo = document.getElementById("producto1");
  var selected = combo.options[combo.selectedIndex].value;

  const btnPut = document.getElementById("put");
}

function hola() {
  const inputPut = document.getElementById("newTitle").value;
  var combo = document.getElementById("producto1");
  var selected = combo.options[combo.selectedIndex].value;
  var id = localStorage.getItem("idTarea");
  axios
    .patch(url1, {
      title: inputPut,
      status: selected,
      idTarea: id,
    })
    .then((resp) => {
      location.reload();
    })
    .catch((error) => {
      console.error(error);
      alert("Ha ocurrido un error al actualizar la tarea");
    });
}
