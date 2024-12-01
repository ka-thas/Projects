import { ReactNode } from "react";

interface Props {
    children: ReactNode;
    text: string;
    //onclick?
}

const Button = ({ children, text }: Props) => {
    return (
        <button type="button" className="btn btn-primary">
            {text}
        </button>
    );
};

export default Button;
