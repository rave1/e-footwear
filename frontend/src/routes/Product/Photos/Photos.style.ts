import styled from "styled-components";

export const StyledPhotos = styled.div`
    width:50%;
    height:450px;
    img{
        width:100%;
        height:100%;
        object-fit: cover;
        margin-bottom:15px;
    }
    div{
        display:grid;
        grid-template-columns: repeat(3, calc(33.3% - 10px));
        gap:15px;
        img{
            width:100%;
        }
    }
    @media only screen and (max-width: 1024px){
        width:100%;
        height:450px;
        div{
            display:none;
        }
        
    }
    
`;