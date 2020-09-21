

functionMaster() {
    const[seq, setSeq]=React.useState(-1)
    constdata=[{seq:0,name:'홍길동',age:30,address:'인천'},
    {seq:1,name:'이몽룡',age:24,address:'서울'},
    {seq:2,name:'임꺽정',age:38,address:'시흥'}]
    const click = (event) => {
    setSeq(event.target.getAttribute("seq"));
    }
    
    return(
        <>
        {data.map((value) => {
        return<div onClick={click} seq={value.seq} key={value.seq}>
        {value.name}
        </div>
        })
        }
        <Detail seq={seq}/>
        </>
        )
    }