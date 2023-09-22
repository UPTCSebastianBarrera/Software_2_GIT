// scrip code for chatbot

const AddBtn = document.querySelector(".Add");
const ClearBtn = document.querySelector(".Clear");

const AddQInput = document.querySelector(".AddQInput");
const AddAInput = document.querySelector(".AddAInput");

const SearchQInput = document.querySelector(".SearchQInput");

const QAs = document.querySelector(".QAs");

const AddQ =()=>{

  const AddQInputContent = AddQInput.value;
  // <div class="QA border-2 border border-warning rounded d-flex justify-content-between">
  //   <p class="TaskContent p-2 text-justify">sdasfasf</p> 
  //   <span class="bg-dark border rounded text-white py-3 px-2">X</span>
  // </div>

  const QA = document.createElement("div");
  QA.classList.add("QA","border-2","border","border-warning","rounded","d-flex","justify-content-between");

  const paragraph = document.createElement("p");
  paragraph.classList.add("QAContent","p-2","text-justify");
  paragraph.textContent = AddQInputContent;

  QA.appendChild(paragraph);

  const spna = document.createElement("span");
  spna.classList.add("bg-dark","border","rounded","text-white","py-3","px-2")
  QA.appendChild(spna);

  const a = document.createElement("a");
  a.classList.add("text-decoration-none");
  a.textContent="X";
  spna.appendChild(a);

  QAs.appendChild(QA);
  
}


AddBtn.addEventListener("click", AddQ);