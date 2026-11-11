import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const w=await SpreadsheetFile.importXlsx(await FileBlob.load('work/finance/portfolio_model_selected.xlsx'));
const ranges={'Half budget':'A1:H13','Focus drivers':'A8:B30','Inputs':'A1:I9','Scenarios':'A1:N8','Metrics':'A1:H10','Cash flow build':'A2:H8','H3 horizon':'A1:M4','Read me':'A1:A14'};
await fs.mkdir('tmp/selected_previews',{recursive:true});
for(const [name,range] of Object.entries(ranges)){
 const blob=await w.render({sheetName:name,range,scale:1,format:'png'});
 await fs.writeFile(`tmp/selected_previews/${name.replaceAll(' ','_')}.png`,new Uint8Array(await blob.arrayBuffer()));
}
console.log('Rendered eight supporting views. Portfolio preview already inspected.');
