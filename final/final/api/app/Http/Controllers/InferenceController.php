<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class InferenceController extends Controller
{
    public function performInference(Request $request)
    {
        // Uncomment this part if you want to see the request data
        // dd($request);

        // Retrieve data from the Android app's request
        $data = [
            'diabetic' => $request->input('Diabetic'),
            'alcoholLevel' => $request->input('Alcohol_Level'),
            'weight' => $request->input('Weight'),
            'mriDelay' => $request->input('MRI_Delay')
        ];

        // Prepare the data to be sent to the Python script
        $dataJson = json_encode($data);

        // Run the Python script for inference (uncomment this when you have the script)
        $command = "python /path/to/your/inference.py '$dataJson'";
        $output = shell_exec($command);

        // Return the inference result to the Android app
        return response()->json(['result' => 'Inference result goes here']);
        
    }
}