## FILE: mtDNA_annotator/core.py

cols = row.find_all("td")
if len(cols) > 1 and cols[0].text.strip() == str(pos):
mitomap_note = cols[3].text.strip()
break
except Exception as e:
mitomap_note = f"MITOMAP error: {e}"


clinvar_status = ""
if args.use_clinvar and os.path.exists(args.clinvar):
try:
with open(args.clinvar) as cf:
for line in cf:
if line.startswith("#"):
continue
fields = line.strip().split("\t")
c_pos, c_ref, c_alt = fields[1], fields[3], fields[4]
if c_pos == pos and c_ref == ref and c_alt == alt:
clinvar_status = fields[7]
break
except Exception as e:
clinvar_status = f"ClinVar error: {e}"


result = {
"Sample": sample_id,
"Position": pos,
"REF": ref,
"ALT": alt,
**hmtvar_data,
"MITOMAP_Info": mitomap_note,
"ClinVar_Info": clinvar_status
}
results.append(result)


if args.use_gnomad:
print("\n🔄 Merging with gnomAD...")
gnomad = pd.read_csv(args.gnomad, sep="\t")
gnomad = gnomad.rename(columns={"POS": "Position"})
df = pd.DataFrame(results)
df_merged = df.merge(gnomad, on=["Position", "REF", "ALT"], how="left", suffixes=("", "_gnomAD"))
else:
df_merged = pd.DataFrame(results)


csv_out = args.output_prefix + ".csv"
tsv_out = args.output_prefix + ".tsv"
df_merged.to_csv(csv_out, index=False)
df_merged.to_csv(tsv_out, sep="\t", index=False)


print(f"\n✅ Annotation complete!")
print(f"🔹 CSV saved to: {csv_out}")
print(f"🔹 TSV saved to: {tsv_out}")


try:
print("\n📈 Generating circular mtDNA variant plot...")
circ_fig = plt.figure(figsize=(8, 8))
ax = circ_fig.add_subplot(111, polar=True)


total_len = 16569
radians = df_merged["Position"].astype(int) / total_len * 2 * np.pi


ax.scatter(radians, [1] * len(radians), s=60, alpha=0.8)
ax.set_yticklabels([])
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_title("mtDNA Variant Positions (Circular Plot)", va='bottom')
plt.tight_layout()
plt.savefig(args.output_prefix + "_circular_plot.png")
print(f"🧬 Circular plot saved as {args.output_prefix}_circular_plot.png")
except Exception as e:
print(f"⚠️ Failed to create circular plot: {e}")
