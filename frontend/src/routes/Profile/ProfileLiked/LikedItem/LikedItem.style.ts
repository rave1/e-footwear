import styled from "styled-components";

export const StyledItem = styled.div`
    display:flex;
    img{
        height:150px;
    }
    .info{
        width:100%;
        padding: 5px 25px;
        display:flex;
        justify-content:space-between;
        > div:nth-child(1){
            h4{
                font-size:18px;
                margin-bottom:5px;
            }
            div{
                margin-bottom:3px;
                display:flex;
                p:first-child{
                    margin-right:10px;
                }
            }
            > p:last-child{
                margin-top:30px;
                text-decoration:underline;
                cursor:pointer;
            }
        }
        > h4{
            margin-left:45px;
            font-size:20px;
            letter-spacing:0.3px;
            font-weight:600;
        }
    }
    @media only screen and (max-width:1024px){
        img{
            height:100px;
        }
        .info{
            > div:nth-child(1){
                h4{
                    font-size:14px;
                    margin-bottom:5px;
                }
                p{
                    font-size:12px;
                }
            }
            > h4{
                font-size: 16px;
            }
        }
    }
`;