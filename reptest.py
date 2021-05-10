def mcc(*, tp, tn, fp, fn):
  denom = (tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)
  mcc_score = 0 if denom==0 else (tp*tn-fp*fn)/denom**.5
  return mcc_score
