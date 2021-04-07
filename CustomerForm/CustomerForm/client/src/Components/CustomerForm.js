import { Button,  Form, FormGroup, Input, Label } from 'reactstrap'; 
import { useState } from 'react';
import axios from "axios";
import {API_URL} from "../Constants" 
import './CustomerForm.css';

export default function CustomerForm () {
    const [customer_name, setName] = useState('');
    const [customer_tel, setTel] = useState('');
    const [customer_addr, setAddr] = useState('');
    const [customer_email, setEmail] = useState('');

    const createCustomer = event => {
        axios.post(API_URL, {
            name: customer_name,
            telephone: customer_tel,
            address: customer_addr,
            email: customer_email,
        }).then(()=>{
            setName('');
            setTel('');
            setAddr('');
            setEmail('')
        })
    };

    return (
    <div>
        <Form onSubmit={createCustomer}>    
            <FormGroup>
                <Label for="name">Họ và tên</Label>
                <Input  
                    type="text"
                    name="name"
                    onChange={event => setName(event.target.value)}
                />
            </FormGroup>

            <FormGroup>
                <Label for="telephone">Số điện thoại</Label>
                <Input 
                    type="text"
                    name="telephone"
                    onChange={event => setTel(event.target.value)}
                />
            </FormGroup>

            <FormGroup>
                <Label for="address">Địa chỉ</Label>
                <Input 
                    type="text"
                    name="Address"
                    onChange={event => setAddr(event.target.value)}
                />
            </FormGroup>

            <FormGroup>
                <Label for="email">Email</Label>
                <Input 
                      type="text"
                      name="Email"
                      onChange={event => setEmail(event.target.value)}
                />
            </FormGroup>
            <Button>Gửi</Button>
        </Form>
    </div>
    )
}