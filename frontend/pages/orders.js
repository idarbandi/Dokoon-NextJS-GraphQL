import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './title';

// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod, amount) {
  return { id, date, name, shipTo, paymentMethod, amount };
}

const rows = [
  createData(
    0,
    '14 فروردین، 1404', // 14 Farvardin, 1404 (Solar Hijri calendar)
    'علی رضایی', // Ali Rezaei
    'تهران، ایران', // Tehran, Iran
    'کارت ملی ***-****-****-1234', // National Card (replace * with actual digits)
    1.245.000, // 1,245,000 Iranian Rials
  ),
  createData(
    1,
    '14 فروردین، 1404',
    'فاطمه حسینی', // Fatemeh Hosseini
    'شیراز، ایران', // Shiraz, Iran
    'کارت بانک ملت ****-****-****-9876', // Mellat Bank Card (replace * with actual digits)
    7.890.000, // 7,890,000 Iranian Rials
  ),
  createData(
    2,
    '14 فروردین، 1404',
    'حسن محمدی', // Hassan Mohammadi
    'اصفهان، ایران', // Isfahan, Iran
    'درگاه پرداخت زرین‌پال', // Zarinpal Payment Gateway
    348.500, // 348,500 Iranian Rials
  ),
  createData(
    3,
    '13 فروردین، 1404', // 13 Farvardin, 1404
    'زهرا احمدی', // Zahra Ahmadi
    'مشهد، ایران', // Mashhad, Iran
    'کارت اعتباری صادرات ****-****-****-5678', // Saderat Credit Card (replace * with actual digits)
    2.570.000, // 2,570,000 Iranian Rials
  ),
  createData(
    4,
    '12 فروردین، 1404', // 12 Farvardin, 1404
    'محمد حسین‌پور', // Mohammad Hosseinpour
    'تبریز، ایران', // Tabriz, Iran
    'کیف پول دیجی‌کالا', // Digikala Wallet
    897.200, // 897,200 Iranian Rials
  ),
];

function preventDefault(event) {
  event.preventDefault();
}

export default function Orders() {
  return (
    <React.Fragment>
      <Title>سفارش‌های اخیر</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>تاریخ</TableCell>
            <TableCell>نام</TableCell>
            <TableCell>آدرس ارسال</TableCell>
            <TableCell>روش پرداخت</TableCell>
            <TableCell align="right">مبلغ فروش</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
              <TableCell align="right">{`${row.amount.toLocaleString('fa-IR')} ریال`}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        مشاهده‌ی سفارش‌های بیشتر
      </Link>
    </React.Fragment>
  );
}