import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';
import Title from './title';

// تابع برای ایجاد داده‌ها (حالا با شهرهای ایران)
function createData(city, amount) {
  return { city, amount };
}

// داده‌های فروش برای شهرهای ایران
const salesDataIran = [
  createData('تهران', 12000),
  createData('مشهد', 8500),
  createData('اصفهان', 7200),
  createData('شیراز', 6000),
  createData('تبریز', 5500),
  createData('اهواز', 4800),
  createData('رشت', 3500),
  createData('کرمان', 3000),
];

export default function Chart() {
  const theme = useTheme();

  return (
    <React.Fragment>
      <Title>فروش امروز (به تومان)</Title> {/* Persian title */}
      <ResponsiveContainer>
        <LineChart
          data={salesDataIran} // Use the Iranian data
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <XAxis dataKey="city" stroke={theme.palette.text.secondary} style={theme.typography.body2} />{' '}
          {/* XAxis is now cities */}
          <YAxis stroke={theme.palette.text.secondary} style={theme.typography.body2}>
            <Label
              angle={270}
              position="left"
              style={{
                textAnchor: 'middle',
                fill: theme.palette.text.primary,
                ...theme.typography.body1,
              }}
            >
              مبلغ فروش (تومان) {/* Persian YAxis label */}
            </Label>
          </YAxis>
          <Line
            isAnimationActive={false}
            type="monotone"
            dataKey="amount"
            stroke={theme.palette.primary.main}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </React.Fragment>
  );
}
