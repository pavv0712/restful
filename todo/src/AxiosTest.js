import React from 'react';
import Axios from 'axios'


export default function AxiosTest() {

    const [students, setStudents] = React.useState([]);

    React.useEffect(() =>{
        Axios.get("http://127.0.0.1:8000/api/study/students/")
        .then(res => {
            const {data} = res;
            setStudents(data);
            }).catch(error => {
                console.log(error);
            })
            }, [])

    return(
        <div>
            {
                students.map((v) =>{
                    return <div>{v.name} {v.address} {v.email}</div>
                })
            }
        </div>
    )
}