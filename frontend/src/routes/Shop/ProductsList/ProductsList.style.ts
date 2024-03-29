import styled from "styled-components";

export const StyledList = styled.div`
    width:830px;
    margin-bottom:50px;
    display:grid;
    grid-template-columns: repeat(4, 200px);
    grid-template-rows: repeat(auto-fill, 360px);
    row-gap:15px;
    column-gap:10px;
    @media only screen and (max-width:1440px){
        width:620px;
        grid-template-columns: repeat(3, 200px);
    }
    @media only screen and (max-width: 1024px){
        margin:auto;
    }
    @media only screen and (max-width:768px){
        width:400px;
        grid-template-columns: repeat(2, 200px);
    }
    @media only screen and (max-width:425px){
        width:300px;
        grid-template-columns: repeat(2, 150px);
        grid-template-rows: repeat(auto-fill, 270px);

    }
`;