// scrip code for chatbot

const AddBtn = document.querySelector(".Add");
const ClearBtn = document.querySelector(".Clear");

const AddQInput = document.querySelector(".AddQInput");
const AddAInput = document.querySelector(".AddAInput");

const SearchQInput = document.querySelector(".SearchQInput");

const QAs = document.querySelector(".QAs");

//Permite añadir una pregunta con respuesta al HTML

const AddQ =()=>{

  const AddQInputContent = AddQInput.value;
  // <div class="QA border-2 border border-warning rounded d-flex justify-content-between">
  //   <p class="TaskContent p-2 text-justify">sdasfasf</p> 
  //   <span class="bg-dark border rounded text-white py-3 px-2">X</span>
  // </div>

  const QA = document.createElement("div");
  QA.classList.add("QA","border-2","border","border-warning","rounded","d-flex","justify-content-between");

  const paragraph = document.createElement("p");
  paragraph.classList.add("QAContent","p-2","text-break");
  paragraph.textContent = AddQInputContent;

  QA.appendChild(paragraph);

  const spna = document.createElement("span");
  spna.classList.add("bg-dark","border","rounded","text-white","py-3","px-2")
  QA.appendChild(spna);

  const a = document.createElement("a");
  a.classList.add("text-decoration-none");
  a.textContent="X";
  a.href="#"

  //Permite eliminar preguntas individuales
  a.addEventListener("click", function(){
    QAs.removeChild(QA);
  })


  spna.appendChild(a);

  QAs.appendChild(QA);
  
}

//Permite limpiar el listado de preguntas del HTML

const ClearQ=()=>{

  QAs.textContent="";

}

//Permite buscar una pregunta especifica del listado de HTML
const SearchQ=()=>{

  const paragraphList=document.querySelectorAll(".QAContent");

  console.log(paragraphList);

  paragraphList.forEach(text => {
    if (text.textContent.toLowerCase().includes(SearchQInput.value.toLowerCase())) {
      text.parentElement.classList.remove("d-none");
    } else {
      text.parentElement.classList.add("d-none");
    }
  });

}


AddBtn.addEventListener("click", AddQ);
ClearBtn.addEventListener("click",ClearQ);
SearchQInput.addEventListener("input",SearchQ);