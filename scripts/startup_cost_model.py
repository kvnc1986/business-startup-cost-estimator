#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def subtotal(items, scenario):
    return sum(float(i.get(scenario, 0) or 0) for i in items)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); args=ap.parse_args()
    data=json.loads(Path(args.input).read_text(encoding='utf-8'))
    out={}
    for s in ['minimum','realistic','premium']:
        startup=subtotal(data.get('startup_items',[]),s)
        fixed=subtotal(data.get('monthly_fixed_costs',[]),s)
        variable=subtotal(data.get('monthly_variable_costs',[]),s)
        runway=float(data.get('runway_months',{}).get(s,6))
        cr=float(data.get('contingency_rate',{}).get(s,0.15))
        base=float(data.get('contingency_base',{}).get(s,startup))
        contingency=base*cr
        wc=(fixed+variable)*runway
        fees=float(data.get('financing_fees',{}).get(s,0))
        total=startup+contingency+wc+fees
        revenue=float(data.get('monthly_revenue',{}).get(s,0))
        vc=float(data.get('monthly_variable_costs_at_revenue',{}).get(s,variable))
        cm=((revenue-vc)/revenue) if revenue>0 else None
        be=(fixed/cm) if cm and cm>0 else None
        ticket=float(data.get('average_ticket',{}).get(s,0)); days=float(data.get('trading_days_per_month',30))
        customers=(be/ticket) if be and ticket>0 else None
        out[s]={
          'startup_before_contingency':round(startup,2),'contingency':round(contingency,2),
          'monthly_cash_burn':round(fixed+variable,2),'working_capital':round(wc,2),
          'financing_fees':round(fees,2),'total_funding_requirement':round(total,2),
          'contribution_margin_ratio':round(cm,4) if cm is not None else None,
          'break_even_monthly_revenue':round(be,2) if be else None,
          'break_even_customers_per_month':round(customers,1) if customers else None,
          'break_even_customers_per_day':round(customers/days,1) if customers else None}
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
