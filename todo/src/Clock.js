import React, { useEffect } from 'react';

function Clock() {
    const [date1, setDate1] = React.useState(new Date());

    React.useEffect(() => {
        const timer = setInterval(() => {setDate1(new Date())}, 1000 )
        return () => {
            clearInterval(timer);
        }
        }, [])

    return (
        <>
            {date1.toISOString()}
        </>
    )
}

export default Clock;
